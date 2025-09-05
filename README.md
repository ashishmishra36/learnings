# E-Commerce Application Testing using Page Object Model with PyTest

This project is an automated test suite for an E-Commerce web application perform functional test cases mentioned in testcase.md


---

## 📌 Features

- Follows the Page Object Model for scalable test design
- PyTest-based test execution
- Covers:
  - Launching the E-Commerce application
  - User Registration
  - User Login
- Generates a detailed HTML test report and allure report
- Easy to configure and extend

---

## Instruction
1. git clone https://github.com/ashishmishra36/learnings.git
2. create a virtual environment: python -m venv .venv
3. run this command to activate virtual environment:  source .venv/bin/activate
4. pip install -r requirements.txt
5. cd ecommerce/tests pytest -v -s --html=reports/report.html
6. cd ecommerce/tests && pytest --alluredir reports/results_04292025_01 --clean-reports/results_04292025_01
7. allure serve reports/results_04292025_01

conftest.py fixture (init_driver)
       ↓
request.cls.driver = driver
       ↓
BaseTest (uses fixture)
       ↓
Child Test Class (inherits BaseTest → self.driver available)
       ↓
Page Objects (driver passed via constructor)


## command to execute the test suite

pytest --broswer chrome --headless


## Tools
1. Python 3.x - language used
2. PyTest - Core test framework
3. Selenium WebDriver - For web browser automation.
4. pytest-html (for HTML reports) 
5. Page Object Model - design pattern
6. pytest-xdist - To run pytest in parallel mode
7. Allure pytest - For Detailed reporting
8. logger - for logging 
9. openpyxl - to interact with Excel sheet 


## Ci/CD Architecture:
GitHub Repo  ──(push)──► Jenkins Webhook Trigger (in Docker)
                        └── Jenkins Pipeline (runs in container)
                                  └── Clones repo, runs build/tests
                                         └── generate reports and share over my email
                                                └── store those reports to a s3 and user should be able to access it

## Basic best practices followed
1. no hard coded test data 
2. Externalize test data from csv, json  files
3. Design pattern
4. Reusable code utility and conf.py
5. Reusable page action method kept under base page 
6. test data should be sent from the test only 



## Xpath 
1. //tag[contains(@attribute, 'value')]      ---> 
2. //tag[contains(text(), 'partial text')]   --->
3. //tag[starts-with(@attribute, 'prefix')]  --->
4. //*[contains(@id, 'product')]             --->