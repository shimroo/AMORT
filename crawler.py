from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#global variables


#XPATHs
CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]"

#faceless undetected chrome
print("Starting the driver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--user-data-dir=user_data")
waitTime = 20







#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://chatgpt.com/')
sleep(5)


        
print("Work done.\nQuiting driver")
driver.quit()
