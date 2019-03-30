This project contains the calls for 5 APIs for stackoverflow. It uses python2
The tst folder contains the tests for all the 5 APIs.

This uses the pytest framework for the test to execute.

#To Run the test 
Go to the bin folder and run below 
```
chmod +x installer.sh
./installer.sh
```

# Locally Run

##To Run all the tests 

1) Go to the folder of stackexchange
2) Run the below command - 

```applescript
python2 -m pytest tst --junitsml=result_file_name.xml
```

This will run all the test in tst folder and will generate the result of the test in result_file_name.xml 
file in the current directory 

## To Run the individual test

1) Go to the folder of stackexchange
2) Run the below command - 

```applescript
python2 -m pytest tst/test_get_tag_info_api -k test_tag_info_api_with_valid_tag_name --junitsml=result_file_name.xml
```

## To Run the test in the CI 
Jenkins UserScript
```
cd bin
chmod +x installer.sh
./installer.sh
./run_test.py
```

