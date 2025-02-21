
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
# Define URL
url="https://the-internet.herokuapp.com/forgot_password"
# Instantiate web driver and open chrome browser
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#maximize browser window
driver.maximize_window()
#load webpage
driver.get(url)

#find email
email= driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys("deebiga.chinnappan@gmail.com")

#find retrieve password button
Retrieve_Password_button=driver.find_element(By.XPATH,'//*[@id="form_submit"]')
Retrieve_Password_button.click()
sleep(5)
#parse response from webpage
response =requests.get(url,headers={"Accept":"text/html"})
parsed_response = BeautifulSoup(response.text,"html.parser")
element= driver.find_element(By.CSS_SELECTOR,"body > h1").text
if element == "Internal Server Error":
    print ("Server error,Please try again!")
else:
    print("New password setup link sent to your email")

sleep(5)
#close driver
driver.quit()