from pytest import fixture
from requests import Session
from selenium import webdriver
import json


def json_file():
    pass_file = 'pass.json'
    with open(pass_file) as json_file:
        data = json.load(json_file)
        return data


@fixture
def url():
    file = 'url.txt'
    with open(file) as txt_file:
        data = txt_file.readline()
        return data


@fixture
def login_and_password():
    data = json_file()
    return data


@fixture
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


@fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@fixture
def browser_logged(url, session_logged):
    login_channel = session_logged.cookies.get('LOGIN_CHANNEL')
    login_status = session_logged.cookies.get('LOGIN_STATUS')
    php_sess_id = session_logged.cookies.get('PHPSESSID')

    driver = webdriver.Firefox()

    driver.get(url=url)

    browser.add_cookie({
        'name': 'LOGIN_CHANNEL',
        'value': login_channel
    })
    browser.add_cookie({
        'name': 'LOGIN_STATUS',
        'value': login_status
    })
    browser.add_cookie({
        'name': 'PHPSESSID',
        'value': php_sess_id
    })

    yield driver
    driver.quit()
