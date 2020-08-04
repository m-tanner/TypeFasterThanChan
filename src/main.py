from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
try:
    driver.get("https://www.livechat.com/typing-speed-test/#/")
    assert "Free Typing Speed Test" in driver.title

    entry_field = driver.find_element_by_class_name("test-input")
    while True:
        try:
            next_word = (
                driver.find_element_by_class_name("test-prompt")
                .find_element_by_css_selector("span")
                .get_attribute("innerHTML")
            )

            for character in str(next_word):
                entry_field.send_keys(character)

            entry_field.send_keys(" ")  # send a trailing space to get to the next word

        except NoSuchElementException:
            break  # the site ran out of words!

    sleep(10)  # give some extra time to capture the wonderful results
finally:
    driver.close()
