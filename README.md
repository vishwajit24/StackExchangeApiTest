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

1) Go to the folder of StackExchangeAPITest/bin
2) Run the below command - 

```applescript
python2 run_test.py
```

This will run all the test in tst folder and will generate the result of the test in result.xml 
file in the current directory 

## To Run the test in the CI 
Jenkins UserScript
```
cd bin
chmod +x installer.sh
./installer.sh
python run_test.py
```

