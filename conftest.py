from pytest import fixture
from requests import Session
from selenium import webdriver


@fixture
def url():
    return 'https://www.mycenter.pl/'


@fixture
def session_logged(url):
    session = Session()
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        }
    )
    session.get(url=url)

    login_info = {
        'form': 1,
        'email': 'x',
        'password': 'x'
    }

    session.post(url=f'{url}login.html', data=login_info)

    return session


@fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
