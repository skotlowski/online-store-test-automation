from requests import Session
from pytest import mark


@mark.login
@mark.request
class LoginTests:

    def test_login(self, url, login_and_password):
        session = Session()
        session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            })

        expected_response = 200

        session.get(url=url)
        response = session.post(url=f'{url}/login_check', data=login_and_password)

        assert response.status_code == expected_response
