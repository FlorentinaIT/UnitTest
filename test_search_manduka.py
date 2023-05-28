import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Manduka_Search(unittest.TestCase):


    TRAVEL_MATS = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div/div/div/nav/table/tr/td[1]/a')
    SEARCH = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[5]/div/div[1]/div/form/button')

    def setUp(self):
        '''
        this method defines all the actions to be made before any test
        '''
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://eu.manduka.com")
        self.chrome.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[2]').click()
        self.chrome.implicitly_wait(15)


    def tearDown(self):
        '''
        this method closes the browser after the tests are made
        '''
        self.chrome.quit()

    def test_search_text(self):
        '''
        check if searching a certain text gets you to a page that contains that certain text
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('travel')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        expected = 'TRAVEL MATS'
        actual = self.chrome.find_element(*self.TRAVEL_MATS).text
        self.assertEqual(expected, actual)