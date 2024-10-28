from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#global variables
playlists = []
with open("playlists.txt", "r") as file:
    playlists = file.readlines()
    playlists = [playlist.strip() for playlist in playlists]


urlDict = {}
with open("urlDict.json", "r") as file:
    try:
       urlDict = json.load(file)
    except:
        print("Running for the first time.")
   

#XPATHs
# VideoSection = "//div[contains(@id,'content') and contains(@class,'ytd-playlist-video-list-renderer')]"
# VideoInfoN = "(//a[contains(@id,'video-title') and contains(@class,'yt-simple-endpoint style-scope ytd-playlist-video-renderer')])"
VideoInfoN = "(//div[contains(@id,'content') and contains(@class,'ytd-playlist-video-list-renderer')]//a[contains(@id,'video-title') and contains(@class,'yt-simple-endpoint style-scope ytd-playlist-video-renderer')])"

#faceless undetected chrome
print("Starting the driver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--user-data-dir=user_data")
# options.add_argument("--headless")
waitTime = 10



def getUrl(url):

    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/watch?v={video_id}"
    
    return None



#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

for playlist in playlists:

    try:
        driver.get(playlist)
    except Exception as e:
        print(f"Error: Invalid playlist URL")
        continue

    videoCount = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, VideoInfoN))))
    print(f"Working on playlist {playlist} with {videoCount} videos")


    for i in range(videoCount):

        videoInfo = wait.until(EC.presence_of_element_located((By.XPATH, VideoInfoN + "[" + str(i+1) + "]" )))
        
        video_title = videoInfo.get_attribute("title")
        video_url = videoInfo.get_attribute("href")
        video_url = getUrl(video_url)

        if video_url in urlDict.values():
            print(f"\tAlready have {video_title}")
        else:
            print(f"\tsaved {video_title[:40]} = {video_url}")
            urlDict[video_title] = video_url


    with open("urlDict.json", "w") as file:
        json.dump(urlDict, file, indent=4)

    print(f"Done with {playlist}")


print("Work done.\nQuiting driver")
driver.quit()
