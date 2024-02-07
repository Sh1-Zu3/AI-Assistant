from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import cv2

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

video ='fade alan walker'
# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element(By.ID, "video-title").click()


all_iframes = driver.find_elements("name","iframe")
if len(all_iframes) > 0:
    print("Ad Found\n")
    browser.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    print('Total Ads: ' + str(len(all_iframes)))
else:
    print('No frames found')


#like_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"(//yt-icon[@class='style-scope ytd-toggle-button-renderer'])[4]")))
#like_btn.click()

# won't work unless you are logged in
#dislike_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"(//yt-icon[@class='style-scope ytd-toggle-button-renderer'])[5]")))
#dislike_btn.click()

def pause():
    pause_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Pause (k)']")))
    pause_btn.click()

# comment out to test pause btn, otherwise it happens so fast you don't notice
def play():
    play_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Play (k)']")))
    play_btn.click()

def mute():
    mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Mute (m)']")))
    mute_btn.click()

# comment out to test mute_btn, otherwise it happens so fast you don't notice it
def unmute():
    unmute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Unmute (m)']")))
    unmute_btn.click()

def exit():
    driver.close()