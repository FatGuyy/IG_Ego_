from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Select the driver, In our case we will use Chrome.
chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(input('Username: '))

password = webdriver.find_element_by_name('password')
password.send_keys(input('Password:'))

#instead of searching for the Button (Log In) you can simply press enter when you already selected the password 
#or the username input element.
submit = webdriver.find_element_by_tag_name('form')
submit.submit()