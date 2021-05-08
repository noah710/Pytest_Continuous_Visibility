# Pytest SMS continuous visibility server
I created this server after creating the pytest testrunnner with testrail reporting. This server can be used to allow continuous visibility on critical tests. 
<br>The server runs the specified tests on a specified interval, and sends a SMS notification to a list of specified phone numbers after the test fails twice. The server will continue attempting the culprit tests, and will notify the specified numbers when the test is resolved. 

# Usage
1. Place pytests in tests directory
2. Fill out parameters in server_params.yaml
3. Run `./deploy.sh` to build and run the Docker Containers