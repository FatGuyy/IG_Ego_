from ast import Global
from re import T
from openpyxl import workbook, load_workbook
from logging import exception
import time
import os 
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def button_click(xpath):
    button = driver.find_element(by=By.XPATH, value=xpath)
    button.click()

def not_following_back(followers_list,following_list):
    return list(set(following_list)- set(followers_list))

dont_restart = False
while dont_restart != True:
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
            #click login buttom
            button_click('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
            #print('3')
        except exception as e:
            print('Unable to login.')
            #print('4')
        
        try:
            driver.implicitly_wait(10)
            #/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input
            search = driver.find_element(by=By.XPATH,  value='/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
            search.send_keys('laughing__soul__')
        except:
            print("Couldn't search.")
        
        #click first profile
        button_click('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        
        followers_count = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
        followers_count = int(followers_count.text)
        
        #click followers button
        button_click('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        
        #scroll The followers tab
        fBody  = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        scroll = 0
        while scroll < (followers_count*0.209): #This may vary as per your connection.
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2) #Increase this sleep if your connection is slow
            scroll += 1
        followers = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div')
        
        #Gets the name of follower
        print('Getting the followers list...')
        
        #sum = 0
        followers_list = []
        for i in range(1,(followers_count+1)):
            x_path = str(f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a/span')
            #sum += 1
            try :
                follower = driver.find_element(by=By.XPATH, value=x_path)
                followers_list.append(follower.text)
            except:
                continue
            driver.implicitly_wait(1)
        print(followers_list)
        #print(sum)
        
        print('Working on following...')

        #click the cross to close followers tab + get the following_count
        button_click('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button')
        time.sleep(4)
        following_count = int(driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span').text)
        #print(following_count)

        #Open following
        #clicking following button
        button_click('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]')

        #Scroll The following popup
        fBody2  = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]')
        scroll = 0
        while scroll < (following_count*0.209): #This may vary as per your connection.
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody2)
            time.sleep(2)  #Incrase this sleep if your connection is slow
            scroll += 1
        print('Done with scrolling')

        #Append in the list
        following_list = []
        for i in range(1,(following_count+1)):
            x_path = str(f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a/span')
            #sum += 1
            try :
                following = driver.find_element(by=By.XPATH, value=x_path)
                #print(following.text)
                following_list.append(following.text)
            except:
                print('Not found')
                dont_restart = False
                continue
            #driver.implicitly_wait(1)
        print(following_list)
        
        #Compare followers and following,store in a list
        not_following = []
        larger_count = 0
        if followers_count>following_count:
            larger_count = followers_count
        else:
            larger_count = following_count

        following_list.sort()
        followers_list.sort()
        try:
            not_following = not_following_back(followers_list,following_list)
        #    for i in range(larger_count):
        #        for follower in followers_list:
        #            if follower == following_list[i]:
        #                not_following.append(follower)
            #dont_restart = True
        except:
            print('some error occurred while scraping following.', 'Restarting the bot...')
            dont_restart = False
        print(not_following)


        #store the list in excel
        wb = load_workbook('Non_followers.xlsx')
        sheet = wb.active
        sheet.append(not_following)

        #laughing__soul__
        

    finally:
        time.sleep(3)
        driver.quit()
