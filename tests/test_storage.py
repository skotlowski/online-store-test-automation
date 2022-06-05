from pytest import mark
from selenium.webdriver.common.by import By


@mark.browser
def test_storage_add_new_item(url, browser_logged):
    browser = browser_logged

    # Clean storage, this method is not working on website - bug
    # clear_storage(browser, url)

    # Navigate to TV section
    browser.get(url=f'{url}/telewizory-i-rtv/telewizory')

    # Add first item to storage
    browser.find_element(by=By.CSS_SELECTOR, value="[class='c-offerBox_photo'").click()
    expected_item = browser.find_element(by=By.CSS_SELECTOR, value="[class='a-typo is-primary'").text
    browser.find_element(by=By.CSS_SELECTOR, value="[class ='c-btn is-link is-addToWishlist'").click()

    # Navigate to storage
    browser.get(url=f'{url}/ulubione/storage')
    item = browser.find_element(by=By.CSS_SELECTOR, value="[class='a-typo is-text'").text
    browser.find_element(by=By.CSS_SELECTOR, value="[class='c-btn is-link is-remove'").click()

    assert expected_item == item


def clear_storage(browser_logged, url):
    browser = browser_logged
    # Navigate to storage
    browser.get(url=f'{url}/ulubione/storage')
    # Remove all items from storage
    browser.find_element(by=By.CSS_SELECTOR, value="[class='c-btn is-link is-wishlistRemoveAll'").click()

