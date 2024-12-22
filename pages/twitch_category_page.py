from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TwitchCategoryPage(BasePage):
    STREAMER = (By.XPATH, '//button[contains(@class, "ScCoreLink-sc")]')

    def assert_streamers_are_visible(self):
        assert self.find_elements(self.STREAMER), "No streamers found on the page"
    
    def select_random_streamer_on_page(self):
        for streamer in self.find_elements(self.STREAMER):
            if self.is_element_in_viewport(streamer):
                streamer.click()
                break
