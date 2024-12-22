from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TwitchStreamerPage(BasePage):
    WARNING_POPUP = (By.XPATH, '//div[@data-a-target="content-classification-gate-overlay"]')
    WARNING_POPUP_APPLY_BUTTON = (By.XPATH, '//button[@data-a-target="content-classification-gate-overlay-start-watching-button"]')
    LOADING_SPINNER = (By.XPATH, '//div[contains(@class, "ScLoadingSpinnerCircle")]')
    
    def wait_for_video_to_load(self):
        self.wait_for_element_disappear(self.LOADING_SPINNER)

    def close_warning_popup_if_exist(self):
        if self.find_elements(self.WARNING_POPUP):
            self.click(self.WARNING_POPUP_APPLY_BUTTON)
            self.wait_for_element_disappear(self.WARNING_POPUP)
