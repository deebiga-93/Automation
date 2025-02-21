from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url="https://the-internet.herokuapp.com/dynamic_loading/2"
driver.maximize_window()
driver.get(url)
wait=WebDriverWait(driver,10)
sleep(3)
#find the startbutton
Start_button=driver.find_element(By.XPATH,'//*[@id="start"]/button').click()
sleep(9)
if driver.find_element(By.XPATH,'//*[@id="finish"]/h4'):
  print ("Element exist!")
sleep(5)
driver.quit()