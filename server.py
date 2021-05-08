from twilio.rest import Client
from datetime import datetime, timedelta
import os
import time
import yaml

# creates a list of all absolute paths
def tests_to_list(path):
    test_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                test_list.append(os.path.join(root, file))
    return test_list

def main():
    # load in all params
    with open('/server_params.yaml') as f:
        params = yaml.load(f, Loader=yaml.FullLoader)
        print(params)
        print(params.get('SMS_reporting_numbers'))

    # load all test to run
    test_list = tests_to_list(params.get('tests_path'))

    # get twilio client 
    twilio_client = Client(params.get('twilio_sid'), params.get('twilio_auth_token'))


    # Server states:
    # 1 - Success:              All is well
    # 2 - Intermediate Failure: A test has failed, need to run again 
    # 3 - Failure:              A test has failed twice, need to send text
    # 4 - Recover:              Failing test is passing, need to send text               
    state = 1
    failing_tests = [] # hold tests that are failing
    
    # setup interval to run tests on
    # Only state 1 adhere to this interval, all other states run as fast as possible
    nextRunTime = datetime.now() + timedelta(minutes=params.get('interval'))
    # loop
    while 1:
        # run each test
        # if a test fails:
        # add it to the failing list and enter intermediate failure state
        if state == 1:
            # this ensures tests run on interal
            while(datetime.now() < nextRunTime):
                time.sleep(1)

            for test in test_list:
                result = os.system('pytest {}'.format(test))
                if result == 0: # if pytest exit without error
                    continue
                else:
                    failing_tests.append(test)
                    state = 2
            nextRunTime = datetime.now() + timedelta(minutes=params.get('interval'))

        elif state == 2:
            # adding this so you can cntl+c before the subprocess starts
            time.sleep(1)

            # run each test that failed
            # if the test passes, remove it from failing list
            # if the test fails, enter failure state
            for test in failing_tests:
                result = os.system('pytest {}'.format(test))
                if result == 0: # if pytest exit without error
                    failing_tests.remove(test)
                else:
                    state = 3

            # if the failing test(s) passed, return to success state
            # this logic captures edge case where 2 tests fail, and 1 test pass in intermediate fail
            if len(failing_tests) == 0:
                state = 1

        elif state == 3:
            # adding this so you can cntl+c before the subprocess starts
            time.sleep(1)
            
            # for each failure, send failure notification
            # move to recover stage
            for test in failing_tests:
                message = params.get('failure_SMS_msg') + test
                for phone in params.get('SMS_reporting_numbers'):
                    twilio_client.messages.create(body=message, from_="+17242091057", to=phone)
            state = 4

        elif state == 4:
            # adding this so you can cntl+c before the subprocess starts
            time.sleep(1)
            
            # run the failing tests until they pass
            # send text when each test pass again
            # if all tests pass, enter success state
            for test in failing_tests:
                result = os.system('pytest {}'.format(test))
                if result == 0: # if pytest exit without error
                    message = params.get('recover_SMS_msg') + test
                    for phone in params.get('SMS_reporting_numbers'):
                        twilio_client.messages.create(body=message, from_="+17242091057", to=phone)
                    failing_tests.remove(test)
                if len(failing_tests) == 0:
                    state = 1




if __name__ == "__main__":
    main()