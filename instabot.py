from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

email = input("Enter the email: ")
pass = input("Enter the password: ")
nooffollowers = int(input("Enter the number of people to follow: "))

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
driver.get("https://www.instagram.com/")

time.sleep(5)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(email)
password.send_keys(pass)
password.submit()

time.sleep(5)


login_info = driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF").click()
time.sleep(10)
notif = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(5)
suggesion = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
time.sleep(5)
for i in range(0,nooffollowers):
    suggesion = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
    time.sleep(3)

