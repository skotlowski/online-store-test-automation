from requests import Session


def test_login_and_inject_cookies_to_browser(url, login_and_password, browser):
    session = Session()
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        })


    expected_response = 200
    session.get(url=url)
    response = session.post(url=f'{url}/login_check', data=login_and_password)

    LOGIN_CHANNEL = session.cookies.get('LOGIN_CHANNEL')
    LOGIN_STATUS = session.cookies.get('LOGIN_STATUS')
    PHPSESSID = session.cookies.get('PHPSESSID')

    assert response.status_code == expected_response

    browser.get(url=url)

    browser.add_cookie({
        'name': 'LOGIN_CHANNEL',
        'value': LOGIN_CHANNEL
    })
    browser.add_cookie({
        'name': 'LOGIN_STATUS',
        'value': LOGIN_STATUS
    })
    browser.add_cookie({
        'name': 'PHPSESSID',
        'value': PHPSESSID
    })

    browser.get(f'{url}/profile')

    expected_response = 'Zmień hasło'
    assert expected_response in browser.page_source


