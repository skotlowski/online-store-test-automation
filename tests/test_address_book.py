from pytest import mark
from selenium.webdriver.common.by import By


@mark.test
@mark.address
@mark.browser
class StorageRequestTests:

    def test_storage_add_new_address(self, browser_logged, url):
        browser = browser_logged
        browser.get(f'{url}/profile/address/new')
        browser.implicitly_wait(1)
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_name').clear()
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_firstName')\
            .clear()
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_lastName') \
            .clear()
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_email') \
            .clear()
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_name')\
            .send_keys('main_address')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_firstName') \
            .send_keys('Jan')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_lastName') \
            .send_keys('Kowalski')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_email') \
            .send_keys('jan.kowalski@gmail.com')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_phone') \
            .send_keys('666999666')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_postcode') \
            .send_keys('33100')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_city') \
            .send_keys('Warszawa')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_street') \
            .send_keys('Warszawska')
        browser.find_element(by=By.CSS_SELECTOR, value='#enp_customer_form_type_address_relation_address_houseNumber') \
            .send_keys('23')
        browser.find_element(by=By.CSS_SELECTOR, value='input[type="submit"').click()
