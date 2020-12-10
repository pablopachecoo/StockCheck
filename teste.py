import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TwitterBot():
    def __init__(self,username,password):
        self.browser = uc.Chrome()
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.twitter.com/login")
        time.sleep(5)
        usernameInput=self.browser.find_element_by_name("session[username_or_email]")
        passwordInput=self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
if __name__=="__main__":
    username= input("Enter your username: ")
    password= input("Enter your password: ")
    t=TwitterBot(username,password)
    t.signIn()