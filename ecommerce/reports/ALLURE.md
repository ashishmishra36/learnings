 ## steps to install Allure reporting - Windows 

1. open https://scoop.sh/ in browser and powershell in windows run below command - "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression 
2. close the powershell and open a new window 
3. Install java if not present in  the machine
4. Run command : scoop install allure and check version allure --version
5. go to the test directory and run command: pytest --alluredir reports/results_04182025_01 --clean-reports/results_04292025_01
6. generate allure report : allure serve reports/results_04292025_01


## steps to install allure in mac
1. 