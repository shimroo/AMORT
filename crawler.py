from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


#global variables
# load songs name from the txt file
songs = []
with open("songs.txt", "r") as file:
    songs = file.readlines()
    songs = [song.strip() for song in songs]


#load the song dictionary
songDict = {}
with open("songDict.json", "r") as file:
    try:
       songDict = json.load(file)
    except:
        print("Running for the first time.")
   

#XPATHs
SearchBar = "//input[contains(@id,'search')]"
FirstResult = "(//ytd-thumbnail[contains(@size,'large')])"
# CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]"
CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]//span[contains(@class,'yt-core-attributed-string--white-space-pre-wrap' )]"


#faceless undetected chrome
print("Starting the driver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--user-data-dir=user_data")
waitTime = 30




#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://www.youtube.com/')


for song in songs:
    if song in songDict:
        print(f"Skipping {song}")
        continue
    print(f"Searching for {song}")
    search = wait.until(EC.presence_of_element_located((By.XPATH, SearchBar)))
    search.clear()
    search.send_keys(song)
    search.submit()
    
    try:
        result = wait.until(EC.element_to_be_clickable((By.XPATH, FirstResult+"[1]")))
    except:
        try:
            result = wait.until(EC.element_to_be_clickable((By.XPATH, FirstResult+"[2]")))
        except:
            result = wait.until(EC.element_to_be_clickable((By.XPATH, FirstResult+"[3]")))

    result.click()
    sleep(2)


    # scroll down until the comments are loaded
    actions = ActionChains(driver)
    for _ in range(5):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(1)


    #get first count comments
    count = 100
    comments = []
    retryLimit = 5
    for i in range(count):
        try:
            comment = wait.until(EC.presence_of_all_elements_located((By.XPATH, "("+CommentN+")["+str(i+1)+"]")))
            comments.append(comment[0].text)
            
            if i % 5 == 0:
               actions.send_keys(Keys.PAGE_DOWN).perform()
            
            retryLimit = 5
        except:
            if retryLimit == 0:
                break

            sleep(0.5)
            i -= 1
            retryLimit -= 1
            actions.send_keys(Keys.PAGE_DOWN).perform()
            

    #save the comments in the dictionary 
    songDict[song] = comments
    with open('songDict.json', 'w', encoding='utf-8') as fp:
            json.dump(songDict, fp, ensure_ascii=False, indent=4)

 

    

        
print("Work done.\nQuiting driver")
driver.quit()
