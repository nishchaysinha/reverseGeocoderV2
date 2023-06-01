from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.csvtools import *
from config.configure import *


class reverseGeocoder():
    def __init__(self):
        conf = config()
        self.options = webdriver.ChromeOptions().add_argument('headless').add_argument('no-sandbox').add_argument('disable-dev-shm-usage')
        self.browser = webdriver.Chrome(executable_path=conf["driver_path"], options=self.options)
        self.baseurl = "http://maps.google.com/maps?z=12&t=m&q=loc:"
    
    def get_address(self, lat, lon):
        url = self.baseurl + str(lat) + "+" + str(lon)
        self.browser.get(url)
        address = self.browser.find_element_by_class_name("widget-pane-link").text
        return address
    
        '''self.browser.get(url)
            WebDriverWait(self.browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
            address = self.browser.find_element(By.CLASS_NAME, "LCF4w")
            return address'''
    
    def update_address(self, filename):
        csv = csvtools()
        data = csv.read(filename)
        for i in range(len(data)):
            if i == 0:
                data[i].append("Address")
            else:
                data[i].append(self.get_address(data[i][0], data[i][1]))
        csv.write(filename, data)


    def close(self):
        self.browser.close()
        self.browser.quit()

