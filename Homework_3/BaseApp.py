from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element locator {locator}")

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self, url='https://test-stand.gb.ru'):
        # return self.driver.get(self.base_url)
        return self.driver.get(url)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text
