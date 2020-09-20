import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from acceptance.locators.base_page import BasePageLocators
from acceptance.locators.home_page import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://stats.nba.com'

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def search_text_field(self):
        return self.find_element(BasePageLocators.search_field)

    @property
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

