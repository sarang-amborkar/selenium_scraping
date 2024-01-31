import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_browser_demo():
    # launch the browser
    driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://ebay.com")
    driver.close()


def test_browser_demo():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)
    # send_keys() is for entering text in selected box
    driver.find_element(by=By.NAME, value='username').send_keys('Admin')
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    error_msg = driver.find_element(By.XPATH, "//p[@data-v-87fcf455]").text
    assert error_msg == 'Invalid credentials'
    time.sleep(2)
    driver.find_element(by=By.NAME, value='password').clear()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]' ).send_keys('admin123')

    # we can also use .submit() here
    driver.find_element(By.CSS_SELECTOR, 'button').click()

#locators
# id, name, classname, linktext, partial linktext, tagname
# xpath ( absolute // and relative /) , css selector
# relative locators ( above, below, to left of, to right of , around)

# //div/p[@data-v-87fcf455] where p is <p> tag and <div> tag
# //input[@type='password' and @name='password']
