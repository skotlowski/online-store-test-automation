from requests import Session


def test_login_and_inject_cookies_to_browser(url, browser):
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

    expected_response = 200
    response = session.post(url=f'{url}login.html', data=login_info)
    assert response.status_code == expected_response

    PHPSESSID = session.cookies.get('PHPSESSID')
    ebox_email = session.cookies.get('ebox_email')
    ebox_imie = session.cookies.get('ebox_imie')
    referer_enp = session.cookies.get('referer_enp')
    referer_id = session.cookies.get('referer_id')

    browser.get(url)

    browser.add_cookie({
        'name': 'PHPSESSID',
        'value': PHPSESSID
    })
    browser.add_cookie({
        'name': 'ebox_email',
        'value': ebox_email
    })
    browser.add_cookie({
        'name': 'ebox_imie',
        'value': ebox_imie
    })
    browser.add_cookie({
        'name': 'referer_enp',
        'value': referer_enp
    })
    browser.add_cookie({
        'name': 'referer_id',
        'value': referer_id
    })

    browser.get(f'{url}konto.html')

    expected_response = 'Twoje ostatnie zamówienie'
    assert expected_response in browser.page_source


