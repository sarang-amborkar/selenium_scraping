import time
import urllib.parse
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = os.path.join(os.getcwd(), 'DATA')


def show_group_page(encd, village_name, shgcd,bachat_gat,gp_name):
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.path.join(PATH, village_name,bachat_gat.replace('/','_'))}
    options.add_experimental_option("prefs", prefs)
    encoded_bachat = urllib.parse.quote(bachat_gat)
    gp_name = urllib.parse.quote(gp_name)
    village_name= urllib.parse.quote(village_name)
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.refresh()
    url = f"https://nrlm.gov.in/shgOuterReports.do?methodName=showGroupPage&encd={encd}&srtnm=mh&shgcd={shgcd}&stateName=MAHARASHTRA&districtName=GONDIA&blockName=ARJUNI%20MORGAON&grampanchayatName={gp_name}&villageName={village_name}&groupName={encoded_bachat}"
    try:
        driver.get(url)
    except Exception as e:
        try:
            driver.delete_all_cookies()
            driver.refresh()
            time.sleep(2)
            driver.get(str(url))
        except Exception as e:
            return
    time.sleep(3)
    # Wait for the dropdown to be clickable
    try:
        dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select')))
    except:
        try:
            driver.refresh()
            dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select')))
        except Exception as e:
            print(e)
            return

    dropdown_element.click()
    # Select an option from the dropdown
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text('100')
    # Wait for the "Download as PDF" link to be clickable
    driver.implicitly_wait(20)
    download_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Download as PDF"]/img')))
    download_link.click()
    # Optionally, wait for the download to complete (you may adjust the wait time)
    driver.implicitly_wait(20)
    time.sleep(3)
    # files = glob.glob(os.path.join(PATH + village_name, "*.pdf"))
    # latest_file = max(files, key=os.path.getmtime)
    pdf_files = [file for file in os.listdir(os.path.join(PATH,village_name,bachat_gat.replace('/','_'))) if file.endswith(".pdf")]
    if pdf_files:
        # pdf_files.sort(key=lambda x: os.path.getmtime(os.path.join(PATH,village_name)), reverse=True)
        latest_file = os.path.join(PATH,village_name,bachat_gat.replace('/','_'), pdf_files[0])
        normalized_path = os.path.normpath(latest_file)
        new_file_name = bachat_gat.replace('/','_') + ".pdf"
        try:
            os.rename(normalized_path, os.path.join(PATH , village_name,bachat_gat.replace('/','_'), new_file_name.replace('/','_')))
        except FileExistsError:
            print("already exist")
    driver.close()


if __name__ == '__main__':
    from bachat_gat import bachat_gats
    for bach in bachat_gats:
        show_group_page(bach[0], bach[1], bach[2], bach[3], bach[4].strip())