from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import requests
from bs4 import BeautifulSoup
#define URL
url="https://the-internet.herokuapp.com/dynamic_content"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
wait=WebDriverWait(driver,10)
sleep(3)
response =requests.get(url,headers={"Accept":"text/html"})
parsed_response = BeautifulSoup(response.text,"html.parser")
Before_click= parsed_response.find_all("div",class_="large-10 columns")

#define clickhere button
Click_here_button=driver.find_element(By.XPATH,'//*[@id="content"]/div/p[2]/a')
Click_here_button.click()
sleep(3)
current_url="https://the-internet.herokuapp.com/dynamic_content?with_content=static"
response = requests.get(current_url,headers={"Accept":"text/html"})
Parsed_response1= BeautifulSoup(response.text,"html.parser")
After_click= Parsed_response1.find_all("div",class_="large-10 columns")
sleep(3)
if Before_click == After_click:
    print("It is not Loaded new page")
else:
    print("It Loaded new page")    
driver.quit()