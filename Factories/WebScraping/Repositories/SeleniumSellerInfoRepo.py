
import time
from selenium.webdriver.common.by import By

class SeleniumSellerInfoRepo:

    # init set driver
    def __init__(self,driver):
        self.driver = driver

    # get seller name 
    def __get_seller_name(self):

        return self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/a/div/div[2]/span').text

    # get seller phone
    def __get_seller_phone(self):

        
        if not len(self.driver.find_elements(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/span[2]')):
            phone = 'not available'
        
        elif len(self.driver.find_elements(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/span[2]')):

            self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/span[2]').click()
            time.sleep(1)
            # get phone number
            return self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/span').text

        if not len(self.driver.find_elements(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/span[2]')):
            phone = 'not available'

        elif len(self.driver.find_elements(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/span[2]')):

            self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/span[2]').click()
            time.sleep(1)
            # get phone number
            return self.driver.find_element(By.XPATH,'//*[@id="body-wrapper"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/span').text

        return phone

        
        

        
    # get seller info
    def get_seller_info(self,url):
        time.sleep(1)
        # open item browser
        self.driver.get(url)

        # return seller info
        return self.__get_seller_name() , self.__get_seller_phone()


    

        