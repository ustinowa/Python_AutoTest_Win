import time
import yaml
from testpage import OperationsHelper
import logging


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata["login"]
password = testdata["password"]


def test_step1(browser):
    logging.info("Test1 run")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("test2 running")
    testpage = OperationsHelper(browser)
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f"Hello, {login}"


def test_step3(browser):
    logging.info("test3 running")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("New title")
    testpage.enter_description("New description")
    testpage.enter_content("New content")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == "New title"


def test_step4(browser):
    logging.info("test4 running")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name("test_name")
    testpage.enter_contact_mail("test@test.ru")
    testpage.enter_contact_content("test_content")
    time.sleep(2)
    testpage.click_contact_send_btn()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"

