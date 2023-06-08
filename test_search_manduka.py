import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Manduka_Search(unittest.TestCase):

    TRAVEL_MATS = (By.PARTIAL_LINK_TEXT, 'TRAVEL')
    SEARCH = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[5]/div/div[1]/div/form/button')
    HOUSE_TEE = (By.XPATH, '//*[@id="shopify-section-product"]/div/div/div/div[2]/div[2]/h1')
    ESSENCE_LEGGING = (By.XPATH, '//*[@id="shopify-section-product"]/div/div/div/div[2]/div[2]/h1')
    ESSENCE_BRA = (By.XPATH, '//*[@id="shopify-section-product"]/div/div/div/div[2]/div[2]/h1')

    def setUp(self):
        '''
        this method defines all the actions to be made before any test
        '''
        self.chrome = webdriver.Chrome()
        self.chrome.implicitly_wait(15)
        self.chrome.maximize_window()
        self.chrome.get("https://eu.manduka.com")
        self.chrome.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[2]').click()

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

    def test_no_of_elements_in_list(self):
        '''
        check no of elements/products from list displayed after searching 'clothing'
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list = self.chrome.find_elements(By.XPATH, '//*[@id="kuLandingProductsListUl"]/li')
        expected = 23
        actual = len(list)
        self.assertEqual(expected, actual)

    def test_element_178_in_list(self):
        '''
        check list functionality for search by "clothing" and click on House Tee - Unisex product using
        index of element (177)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[177].click()
        expected = 'HOUSE TEE - UNISEX'
        actual = self.chrome.find_element(*self.HOUSE_TEE).text
        self.assertEqual(expected, actual)

    def test_element_178_on_page(self):
        '''
        check the url after clicking on 178 element from list (with index 177)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[177].click()
        time.sleep(5)
        expected = 'https://eu.manduka.com/products/house-tee?variant=40181264973875'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_element_180_in_list(self):
        '''
        check list functionality for search by "clothing" and click on Essence Legging product using
        index of element (179)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[179].click()
        time.sleep(5)
        expected = 'https://eu.manduka.com/products/essence-legging?variant=40180971667507'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_element_180_on_page(self):
        '''
        check corresponding url for search by 'clothing' and click on Essence Legging product using
        index of element (179)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[179].click()
        expected = 'ESSENCE LEGGING'
        actual = self.chrome.find_element(*self.ESSENCE_LEGGING).text
        self.assertEqual(expected, actual)

    def test_element_185_in_list(self):
        '''
        check list functionality for search by 'clothing' and click on Essence Bra product using
        index of element (184)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[184].click()
        time.sleep(5)
        expected = 'https://eu.manduka.com/products/essence-bra?variant=31569100767283'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_element_185_on_page(self):
        '''
        check corresponding url for search by 'clothing' and click on Essence Bra product using
        index of element (184)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('clothing')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(5)
        list_element = self.chrome.find_elements(By.TAG_NAME, 'li')
        list_element[184].click()
        expected = 'ESSENCE BRA'
        actual = self.chrome.find_element(*self.ESSENCE_BRA).text
        self.assertEqual(expected, actual)

