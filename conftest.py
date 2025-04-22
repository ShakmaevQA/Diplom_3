import pytest
import requests
from selenium import webdriver
from faker import Faker
from config import Endpoints

fake = Faker()

@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Browser {request.param} is not supported")

    driver.get(Endpoints.HOME_PAGE)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def generate_user():
    user_info = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    response = requests.post(Endpoints.SIGN_UP, json=user_info)
    response_content = response.json()

    yield user_info, response_content, response.status_code

    if response.status_code == 200 and response_content.get('success', False):
        token = response_content.get('accessToken')
        if token:
            requests.delete(Endpoints.REMOVE_USER, headers={'Authorization': token})