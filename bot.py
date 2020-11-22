from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Instagrambot:
    #Takes username, password, and logs into the instagram page, with your bot. Create a username and password pls

    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.base="https://www.instagram.com"

        self.driver=webdriver.Chrome("chromedriver.exe")
        self.login()
        
  
    def login(self):
        
        self.driver.get("{}/accounts/login/?hl=en".format(self.base))
        #sending username and password
        enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME,'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME,'password')))
        enter_password.send_keys(self.password)
        #sending login click
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()

        time.sleep(2)
        
        
    def follow_user(self,person):
        #follows user

        self.profile(person) 
    
        try:
            button=self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
            button.click()
        except:
            pass    


        try:
                message_button=self.driver.find_elements_by_xpath("//button[contains(text(),'Message')]")[0]   
        except:
            return
            
        message_button.click()
        self.message()
             
        
   
        
    def message(self):
        btn1=self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        
        btn1.click()

       

    def profile(self,user):
        #goes to page
        self.driver.get("{}/{}/".format(self.base,user)) 
        

if __name__=="__main__":

    chungus=Instagrambot("bigchungus6_9","Chungus@1999")
    chungus.follow_user("kotathefriend")
    
   






    
    
