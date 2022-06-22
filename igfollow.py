from lib2to3.pgen2.driver import Driver
from logging import exception
import time
import os 
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


try:
    os.environ['PATH'] += r'.\chromedriver.chromedriver.exe'
    #chrome_options = Options()
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
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
    
    followers_count = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
    followers_count = int(followers_count.text)
    followers_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
    followers_button.click()
    
    #Gets the name of follower
    #Xpath for the names = /html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div
    #follower = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span')
    #print(follower.text)
    time.sleep(4)
    


    print('Till here')
    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
    print('Till loop')
    FList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))

    FList.click()
    actionChain = webdriver.ActionChains(driver)
    time.sleep(random.randint(2,4))

    while (numberOfFollowersInList < max()):
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()        
        numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))
        time.sleep(0.4)
        print(numberOfFollowersInList)
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()            
        time.sleep(1)
    #laughing__soul__
    

finally:
    time.sleep(10)
    driver.close()