import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_Manduka(unittest.TestCase):

    WHOLESALE = (By.XPATH, '//*[@id="shopify-section-top-bar"]/div/div/div/div/div[1]')
    END_OF_SEASON = (By.XPATH, '//*[@id="top-bar-announcement-carousel-slide01"]/a')
    MY_ACCOUNT = (By.XPATH, '//*[@id="shopify-section-top-bar"]/div/div/div/div/div[3]/a/span')
    SEARCH = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[5]/div/div[1]/div/form/button')
    USERNAME = (By.XPATH, '//*[@id="customer_email"]')
    PASSWORD = (By.XPATH, '//*[@id="customer_password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="customer_login"]/div[3]/div/button')
    MATS = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[1]/a')
    TOWELS = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[2]/a')
    EQUIPMENT = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[3]/a')
    CLOTHING = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[4]/a')
    GIFTS = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[5]/a')
    SALE = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[6]/a/font')
    GUIDANCE = (By.XPATH, '//*[@id="dropdown-desktop"]/ul/li[7]/a')


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

class Test_Home_Page(Test_Manduka):

    def test_page_title(self):
        '''
        This method verifies if the name of the page is correct
        '''
        expected = 'Manduka | Premium Yoga Mats, Yoga Towels and Clothing | Manduka EU'
        actual = self.chrome.title
        self.assertEqual(expected, actual)

    def test_whole_sales(self):
        '''
        check that "Wholesale & teachers" open the login page for wholesale accounts
        '''
        self.chrome.find_element(*self.WHOLESALE).click()
        expected = 'https://euwholesale.manduka.com/account/login'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_end_of_season(self):
        '''
        check that "End of season sale! shop now" open the sale page
        '''
        self.chrome.find_element(*self.END_OF_SEASON).click()
        expected = 'https://eu.manduka.com/pages/sale'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_my_account(self):
        '''
        check that "My Account" button open the login page
        '''
        self.chrome.find_element(*self.MY_ACCOUNT).click()
        expected = 'https://eu.manduka.com/account/login?return_url=%2Faccount'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_search(self):
        '''
        check the usability of search button (introducing text and press search button)
        '''
        self.chrome.find_element(*self.SEARCH).send_keys('travel')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        expected = 'https://eu.manduka.com/pages/yoga-travel-mats'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_mats_page(self):
        '''
        check that "Mats" button open the mats page
        '''
        self.chrome.find_element(*self.MATS).click()
        time.sleep(3)
        expected = 'https://eu.manduka.com/pages/yoga-mats-category'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_towels_page(self):
        '''
        test that when I click on "Towels" element, I can access towel page
        '''
        self.chrome.find_element(*self.TOWELS).click()
        time.sleep(3)
        expected = 'https://eu.manduka.com/collections/yoga-towels'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_equipment_page(self):
        '''
        test that when I click on "Equipment" button, I can access equipment page
        '''
        self.chrome.find_element(*self.EQUIPMENT).click()
        time.sleep(5)
        expected = 'https://eu.manduka.com/collections/yoga-props-accessories'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_clothing_page(self):
        '''
        check that when I click on "Clothing" element I can access clothing page
        '''
        self.chrome.find_element(*self.CLOTHING).click()
        time.sleep(10)
        expected = 'https://eu.manduka.com/pages/apparel'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_gifts_page(self):
        '''
        check that when I click on "Gifts" button I can access gifts page
        '''
        self.chrome.find_element(*self.GIFTS).click()
        time.sleep(10)
        expected = 'https://eu.manduka.com/pages/moms-day-gift-guide'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_sale_page(self):
        '''
        check that when I click on "Sale" element, I can access sale page
        '''
        self.chrome.find_element(*self.SALE).click()
        time.sleep(15)
        expected = 'https://eu.manduka.com/pages/sale'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_guidance_page(self):
        '''
        check that when I click on "Guidance" button I can access guidance page
        '''
        self.chrome.find_element(*self.GUIDANCE).click()
        expected = 'https://eu.manduka.com/'
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)

    def test_sign_in_btn_is_displayed(self):
        '''
        check the presence of 'sign in' button after clicking on "My Account" button
        '''
        self.chrome.find_element(*self.MY_ACCOUNT).click()
        self.assertTrue(
            self.chrome.find_element(By.XPATH, '//*[@id="customer_login"]/div[3]/div/button').is_displayed()
        )