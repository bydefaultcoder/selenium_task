
# ('CaseType', 'Original Application'), ('CaseNumber', '100'), ('CaseYear', '2019')
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def selenium_code():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://cgat.gov.in/#/lucknow/case-status")
    dropdown_element =  driver.find_element(by=By.XPATH,value="//select[@id='caseTypeId']")
    ele1 = Select(dropdown_element)
    ele1.select_by_visible_text("Original Application")

    ele2 = driver.find_element(by=By.XPATH,value="//input[@id='caseNo']")
    ele2.send_keys("100")

    ele3 = driver.find_element(by=By.XPATH,value="//input[@id='caseYear']")
    ele3.send_keys("2019") 

    submit = driver.find_element(by=By.XPATH,value="//button[@type='submit']")
    submit.click()
#   to access the data
    table_xpath = "//div[@class='modal-body']//table"  # Replace 'table_id' with the actual ID or other identifying attribute of the table
    time.sleep(1)
    table_element = driver.find_element(by=By.XPATH,value=table_xpath)
    # table_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))
    rows = table_element.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)
    driver.close()
# 
   
    
selenium_code()    