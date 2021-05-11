# Pytest SMS continuous visibility server
I created this server after creating the [pytest testrunnner with testrail reporting.](https://github.com/noah710/pytest_testrail_testrunner) While the previous server passively reported test results to Testrail, this server  actively reports failure and recovery of tests via SMS. This should be used for only critical tests, while the previous server should be used for all tests. 
<br><br>The server runs the specified tests on a specified interval, and sends a SMS notification (Twilio credentials required) to a list of specified phone numbers after the test enters the failing state. The server will continue attempting the culprit tests, and will send an SMS to notify when the test is resolved. 
# Usage
1. Place pytests in tests directory. (tests will be recursively traversed to find pytests)
2. Fill out parameters in server_params.yaml (twilio credentials, message, SMS receivers, etc)
3. Run `./deploy.sh` to build and run the docker container
