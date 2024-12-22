from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def click_first(self, locator):
        elements = self.find_elements(locator)
        if elements:
            elements[0].click()
        else:
            raise Exception(f"Element {locator} not found")

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_for_element_disappear(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def take_screenshot(self, filename="screenshot.png"):
        self.driver.save_screenshot(filename)
    
    def is_element_in_viewport(self, element):
        return self.driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect();"
            "return ("
            "rect.top >= 0 && "
            "rect.left >= 0 && "
            "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
            "rect.right <= (window.innerWidth || document.documentElement.clientWidth)"
            ");",
            element
        )
