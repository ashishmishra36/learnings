# learnings
Purpose: While brushing up python/automation, I thought of adding all my code to git , so it's better to manage  

Below are the steps I followed to set up Python in my local-
1. Download Python in some /software folder
2. install Python
3. Add path to the environment variable 
4. close the powershell and open it again 
5. clone the branch "learnings "to /codebase directory 
6. in /codebase/learnings directory create a virtual environment using - "python -m venv .venv"
7. run "dir" command to check if its created 
8. Run command - ".venv\Scripts\activate" to activate the virtual environment
9. Now go inside the repo-> where requirement.txt is present 
10. run "pip install -r .\requirements.txt" - > It will download all required packages
11. Run "pytest --version" command to check if pytest is installed correctly

** About Pytest **
test with a given keyword: pytest -k login -v | Output: will pick all test which have keyword 'login' -v means - more verbose
Parallel execution: pytest -n 5
html report: pytest test_pytest.py -v -s --html=report.html || -s means no print output in the report just in the terminal
We can keep the init_driver fixture in the class or in the conftest.py to make global 



