from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TwitchHomePage(BasePage):
    SEARCH_ICON = (By.XPATH, '//a[@href = "/directory"]//*[local-name() = "svg"]')

    def click_search_icon(self):
        self.click(self.SEARCH_ICON)
