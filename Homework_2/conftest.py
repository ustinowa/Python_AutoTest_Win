import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
login = testdata["login"]


@pytest.fixture()
def sel_1():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def x_selector2():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def x_selector3():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def result():
    return '401'


@pytest.fixture()
def auth():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def result2():
    return f'Hello, {login}'


@pytest.fixture()
def btn_post():
    return '//*[@id="create-btn"]'


@pytest.fixture()
def sel_title():
    # return '//*[@id="create-item"]/div/div/div[1]/div/label'
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def sel_desc():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


@pytest.fixture()
def sel_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


@pytest.fixture()
def result3():
    return 'my test title'


@pytest.fixture()
def btn_safe():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/span'


@pytest.fixture()
def sel_title_check():
    return '//*[@id="app"]/main/div/div[1]/h1'
