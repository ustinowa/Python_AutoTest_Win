import json

import requests

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    with open("config.yaml", "r") as f:
        d = yaml.safe_load(f)

    #ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word, description="title")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], word, description="description")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="contact name")

    def enter_contact_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_MAIL"], word, description="contact mail")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word, description="contact content")

    def auth(self):
        return self.find_element(TestSearchLocators.ids["LOCATOR_AUTH"]).text

    #CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new post")

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save")

    def click_contact_send_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND"], description="send")

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")

    #GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error label")

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"], description="username")

    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RES_LBL"], description="result")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    #API
    def auth_site(self):
        data = {
            "username": self.d["username"],
            "password": self.d["password"]
        }
        res = requests.post(url=self.d["url_auth"], data=json.dumps(data))
        return res.status_code, res.json()["token"]

    def create_post(self):
        headers = {
            "X-Auth-Token": self.auth_site()[1]
        }
        data = {
            "title": "my_title",
            "description": "my_description",
            "content": "my_content",
        }
        res = requests.post(url=self.d["url_create"], headers=headers, data=data)
        return res.json()["description"]



