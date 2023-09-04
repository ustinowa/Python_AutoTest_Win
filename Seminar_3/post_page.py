import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class AddPostLocators:
    LOCATOR_ADD_POST = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label')
    LOCATOR_DESCRIPTION = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_CREATE_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_CHECK_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')


class OperationAddPost(BasePage):
    def add_post(self):
        logging.info("Add post")
        add_post_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST)
        add_post_btn.click()

    def post_context(self, title=None, description=None, content=None):

        title_field = self.find_element(AddPostLocators.LOCATOR_TITLE)
        # title_field.clear()
        if title:
            logging.info(f'fill post: {title}')
            title_field.send_keys(title)
        description_field = self.find_element(AddPostLocators.LOCATOR_DESCRIPTION)
        # description_field.clear()
        if description:
            logging.info(f'fill post: {description}')
            description_field.send_keys(description)
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTENT)
        # content_field.clear()
        if content:
            logging.info(f'fill post: {content}')
            content_field.send_keys(content)
        btn = self.find_element(AddPostLocators.LOCATOR_CREATE_POST)
        btn.click()

    def check_post(self):
        logging.info("Checking new post...")
        time.sleep(2)
        return self.find_element(AddPostLocators.LOCATOR_CHECK_POST).text
