from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from .Repositories.SeleniumSellerInfoRepo import SeleniumSellerInfoRepo

class SeleniumSellerInfo:

    
    def __init__(self,phone,password):

        self.phone = phone

        self.password = password

        chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                              # and if it doesn't exist, download it automatically,
                                              # then add chromedriver to path
        self.driver = webdriver.Chrome()


    def __click_login(self):
        # open browser
        self.driver.get("https://www.olx.com.eg/en/")

        time.sleep(1)
        # click Login
        login_button = self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div[1]/header/div/div[4]/div/button')
   
        login_button.click()

        print("CLICK LOGIN DONE")


    def __post_phone(self):
        # Phone text input
        phone_text_input = self.driver.find_element(By.ID,'phone')

        # add phone to input
        phone_text_input.send_keys(self.phone)

        # submit form
        phone_text_input.send_keys(Keys.ENTER)

        print("POST PHONE DONE")


    def __post_password(self):
        # password text input
        password_text_input = self.driver.find_element(By.ID,'password')

        # add password to input
        password_text_input.send_keys(self.password)

        # submit form
        password_text_input.send_keys(Keys.ENTER)

        print("POST PASSWORD DONE")



    def login(self):

        # login 
        self.__click_login()

        time.sleep(1)
        # post phone
        self.__post_phone()
        
        time.sleep(1)
        # post password
        self.__post_password()

        time.sleep(1)

    def get_seller_info(self,url):
        
        # create repo object
        info_component = SeleniumSellerInfoRepo(self.driver)

        # get phone and name
        phone , name = info_component.get_seller_info(url)
        
        # return phone and name
        print("GOT INFO DONE")

        return {'phone':phone,'name':name}
