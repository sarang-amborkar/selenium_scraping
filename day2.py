
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_alert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://javascript.info/alert-prompt-confirm")
    driver.find_element(By.XPATH, "//div[@id='5qi69jzhsr']//a").click()
    # driver.switch_to.alert.accept()
    driver.switch_to.alert.dismiss()
    time.sleep(10)
