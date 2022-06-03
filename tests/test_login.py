from requests import Session
from pytest import mark


@mark.browser
@mark.request
def test_login_and_inject_cookies_to_browser(url, login_and_password, browser):
    session = Session()
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        })

    expected_response = 200

    session.get(url=url)
    response = session.post(url=f'{url}/login_check', data=login_and_password)

    login_channel = session.cookies.get('LOGIN_CHANNEL')
    login_status = session.cookies.get('LOGIN_STATUS')
    php_sess_id = session.cookies.get('PHPSESSID')

    assert response.status_code == expected_response

    browser.get(url=url)

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

    browser.get(f'{url}/profile')

    expected_response = 'Zmień hasło'
    assert expected_response in browser.page_source


