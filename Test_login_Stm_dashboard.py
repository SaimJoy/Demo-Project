from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


class Teststm():
    def launch_chrome(self):
        # option1=webdriver.ChromeOptions()
        # option1.add_argument("--disble-notification")
        driver = webdriver.Chrome(executable_path="E:\Practice_Selenium\Drivers\chromedriver.exe")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(1)
        # driver.get("https://www.google.com/")
        driver.get("https://corporate-stag.web.app/login")

        # locate element
        username = driver.find_element(By.XPATH, '//*[@id="email"]')
        password = driver.find_element(By.XPATH, '//*[@id="psw"]')
        login = driver.find_element(By.CLASS_NAME, 'btn')

        # sending login Credentials
        # TestCase_Login
        username.send_keys('dr_nazmul')
        password.send_keys('123456')


        # Click the login button using JavaScript
        driver.execute_script("arguments[0].click();", login)
        time.sleep(7)

        # TestCase_Page navigate
        serve_patient = driver.find_element(By.XPATH,'/html/body/app-root/div/app-doctor/app-sidenav/nz-layout/nz-sider/div/ul/ul/li[2]/span')
        driver.execute_script("arguments[0].click();", serve_patient)
        time.sleep(5)

        followup_patient = driver.find_element(By.XPATH, "/html/body/app-root/div/app-doctor/app-sidenav/nz-layout/nz-sider/div/ul/ul/li[3]")
        driver.execute_script("arguments[0].click();" ,followup_patient)
        time.sleep(5)

        canc_ref = driver.find_element(By.XPATH, "/html/body/app-root/div/app-doctor/app-sidenav/nz-layout/nz-sider/div/ul/ul/li[4]")
        driver.execute_script("arguments[0].click();", canc_ref)
        time.sleep(5)

        sec_ref = driver.find_element(By.XPATH, "/html/body/app-root/div/app-doctor/app-sidenav/nz-layout/nz-sider/div/ul/ul/li[5]")
        driver.execute_script("arguments[0].click();", sec_ref)
        time.sleep(5)

        #Testcase_log out
        #log_out =driver.find_element(By.XPATH, "/html/body/app-root/div/app-doctor/app-sidenav/nz-layout/nz-sider/div/ul/ul/li[55]/span")
        #driver.execute_script("arguments[0].click();", log_out)
        #time.sleep(5)


chrome_obj = Teststm()
chrome_obj.launch_chrome()
