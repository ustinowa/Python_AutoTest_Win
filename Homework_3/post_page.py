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
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_MAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


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

    def contact_us(self, name, email, content):
        logging.info("Click link Contact us")
        contact_link = self.find_element(AddPostLocators.LOCATOR_CONTACT_BTN)
        contact_link.click()
        logging.info(f"Send {name}  to element {AddPostLocators.LOCATOR_CONTACT_NAME[1]}")
        name_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_NAME)
        name_field.clear()
        name_field.send_keys(name)
        logging.info(f"Send {email}  to element {AddPostLocators.LOCATOR_CONTACT_MAIL[1]}")
        mail_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_MAIL)
        mail_field.clear()
        mail_field.send_keys(email)
        logging.info(f"Send {content}  to element {AddPostLocators.LOCATOR_CONTACT_CONTENT[1]}")
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTACT_CONTENT)
        content_field.clear()
        content_field.send_keys(content)
        logging.info("Click send contact button")
        btn_send = self.find_element(AddPostLocators.LOCATOR_CONTACT_SEND)
        btn_send.click()

    def get_alert(self):
        logging.info("Get alert text")
        # text = self.get_alert_text()
        # logging.info(text)
        alert = self.driver.switch_to.alert
        return alert.text

