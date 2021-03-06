from pytest import fixture
from requests import Session
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json


def json_file():
    pass_file = 'pass.json'
    with open(pass_file) as json_file:
        data = json.load(json_file)
        return data


@fixture(scope='session')
def url():
    file = 'url.txt'
    with open(file) as txt_file:
        data = txt_file.readline()
        return data


@fixture(scope='session')
def login_and_password():
    data = json_file()
    return data


@fixture(scope='session')
def session_logged(url, login_and_password):
    session = Session()
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        }
    )
    session.get(url=url)
    session.post(url=f'{url}/login_check', data=login_and_password)
    return session


@fixture(scope='session')
def browser_logged(url, login_and_password):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url=url)
    driver.get(url=f'{url}/login')
    driver.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_login_username')\
        .send_keys(login_and_password.get('enp_customer_form_login[username]'))
    driver.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_login_password')\
        .send_keys(login_and_password.get('enp_customer_form_login[password]'))
    driver.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]').click()
    driver.implicitly_wait(1)
    driver.find_element(by=By.CSS_SELECTOR, value='.c-alert_close').click()
    yield driver
    #driver.quit()


@fixture(scope='function')
def browser_logged_with_requests(url, session_logged):
    login_channel = session_logged.cookies.get('LOGIN_CHANNEL')
    login_status = session_logged.cookies.get('LOGIN_STATUS')
    php_sess_id = session_logged.cookies.get('PHPSESSID')

    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get(url=url)

    driver.add_cookie({
        'name': 'LOGIN_CHANNEL',
        'value': login_channel
    })
    driver.add_cookie({
        'name': 'LOGIN_STATUS',
        'value': login_status
    })
    driver.add_cookie({
        'name': 'PHPSESSID',
        'value': php_sess_id
    })

    driver.find_element(by=By.CSS_SELECTOR, value="[class='c-alert_close'").click()

    yield driver
    driver.quit()


