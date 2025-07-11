import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Basic launch: first way to launch a browser: use the automatic downloaded chromedriver
print('Basic launch: first way to launch a browser: use the automatic downloaded chromedriver')
driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://www.google.com')
assert driver.title=='Google', 'Correct page is not loaded !'
driver.quit()
print('Basic launch: first way  is finished')

# second way to launch a browser: use the explicit manually downloaded chrome driver
# Why ? sometimes chromedriver could not be downloaded at runtime
print('second way: to launch a browser use the explicit manually downloaded chrome driver')
chromedriver_path = Path("resources/chromedriver.exe").resolve()
print(os.path.isfile(chromedriver_path))
service_obj= Service(str(chromedriver_path))
driver1 = webdriver.Chrome(service=service_obj)
driver1.get('https://www.google.com')
assert driver1.title == 'Google', 'Test2: Title is not correct ! '
driver1.quit()
print('Basic launch: second way is finished')


#third way: using webdriver manager which automatically download the chrome driver for the version present in system
# recommended for CI/CD
print('third way: using webdriver manager which automatically download the chrome driver for the version present in system')
obj_service = Service(ChromeDriverManager().install())
driver2=webdriver.Chrome(service=obj_service)
driver2.get('https:www.google.com')
assert driver2.title =='Google', 'Error2: Title is not valid'
driver2.quit()
print('third way: using webdriver manager is finished')


#forth way: Remote launch for docker and Selenium GRID


