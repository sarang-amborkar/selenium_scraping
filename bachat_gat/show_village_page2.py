import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def show_village_page(encd, gp_name):
    driver = webdriver.Chrome()
    driver.get(f"https://nrlm.gov.in/shgOuterReports.do?methodName=showVillagePage&encd={encd.strip()}&stateName=MAHARASHTRA&districtName=GONDIA&blockName=ARJUNI%20MORGAON&grampanchayatName={gp_name.strip()}")
    driver.implicitly_wait(30)
    driver.find_element(By.CSS_SELECTOR, 'select').click()
    dropdown_element = driver.find_element(By.CSS_SELECTOR, 'select')
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text('100')
    driver.implicitly_wait(15)
    # grampachayat villages
    gp_villages = driver.find_elements(By.XPATH,'//*[@id="example"]/tbody/tr/td[2]/a')
    driver.implicitly_wait(15)
    all_gaons = []
    # r"SHGList\('([^']+)',\s*'([^']+)',\s*'([^']+)'\)"
    for area_gaon in gp_villages:
        tag = area_gaon.get_attribute('outerHTML')
        match = re.search(r"SHGList\('([^']+)',\s*'([^']+)',\s*'([^']+)'\)", tag)
        if match:
            all_gaons.append(match.groups())
    return all_gaons


if __name__ == '__main__':
    from village_list import villages
    for item in villages:
        outs = show_village_page(item[0], item[1])
        for out in outs:
            print([out[0], out[2], item[1],item[2]])
