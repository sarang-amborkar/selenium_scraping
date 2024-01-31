import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def show_SHG_page():
    driver = webdriver.Chrome()
    driver.get(f"https://nrlm.gov.in/shgOuterReports.do?methodName=showGPPage&encd=1833007&stateName=MAHARASHTRA&districtName=GONDIA&blockName=ARJUNI%20MORGAON")
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'select').click()
    dropdown_element = driver.find_element(By.CSS_SELECTOR, 'select')
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text('100')
    driver.implicitly_wait(15)
    # arjuni morgon area che gaon
    area_gaons = driver.find_elements(By.XPATH,'//*[@id="example"]/tbody/tr/td[2]/a')
    all_gp = []
    for area_gaon in area_gaons:
        tag = area_gaon.get_attribute('outerHTML')
        match = re.search(r"villageList\('([^']+)',\s*'([^']+)'\)", tag)
        if match:
            all_gp.append(match.groups())
    return all_gp


if __name__ == '__main__':
    all_gp = show_SHG_page()
    print(all_gp)