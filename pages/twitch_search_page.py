from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TwitchSearchPage(BasePage):
    SEARCH_INPUT = (By.XPATH, '//input[@data-a-target = "tw-input"]')
    SEARCH_DROPDOWN = (By.XPATH, '//a[contains(@class, "ScCoreLink")]')

    def search_game_and_select(self, game_name):
        self.input_text(self.SEARCH_INPUT, game_name)
        assert self.find_element(self.SEARCH_DROPDOWN).is_displayed()
        self.click_first(self.SEARCH_DROPDOWN)
