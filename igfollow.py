from logging import exception
import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        driver.implicitly_wait(10)

        username = driver.find_element_by_name('username')
        username.send_keys('fatguy139')
        password = driver.find_element_by_name('password')
        password.send_keys('FatGuy@139')
        print('2')
        submit = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        submit.click()
        print('3')
    except exception as e:
        print('Unable to login.')
        print('4')
    
    try:
        driver.implicitly_wait(10)
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys('laughing__soul__')
    except:
        print("Couldn't search.")
    
    profile = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
    profile.click()
    #Getting the 
    followers_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
    followers_button.click()
        
   
    #laughing__soul__
    

    #followers_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
    #followers_button.click()


finally:
    time.sleep(10)
    #driver.close()