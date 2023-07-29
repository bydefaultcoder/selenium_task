
# ('CaseType', 'Original Application'), ('CaseNumber', '100'), ('CaseYear', '2019')
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

def is_valid_number(num):
    # Regular expression pattern to match a valid positive integer
    integer_pattern = r'^[1-9]\d*$'

    # Check if the input matches the pattern
    if re.match(integer_pattern, num):
        return True
    else:
        return False


def selenium_code(case_type,case_number,case_year):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    try:
       driver.get("https://cgat.gov.in/#/lucknow/case-status")
    except:
        print('website is down')
        driver.quit()
        return {"error":True,"msg":"try again later"}
        

    # for case type
    dropdown_element =  driver.find_element(by=By.XPATH,value="//select[@id='caseTypeId']")
    ele1 = Select(dropdown_element)
    isCaseTypeValid = False
        # cecking case type available or not
    for i in ele1.options:
        if(case_type == i.text):
            isCaseTypeValid= True
            break
    if(not isCaseTypeValid):
        return {"error":True,"msg":"Case type not found"}
        # selecting the case type
    ele1.select_by_visible_text(case_type)

    # putting case number

    if(not is_valid_number(case_number)):
         return {"error":True,"msg":"Case Number is not valid"}

    if(not is_valid_number(case_year)):
         return {"error":True,"msg":"Case year is not alid"}

    ele2 = driver.find_element(by=By.XPATH,value="//input[@id='caseNo']")
    ele2.send_keys(case_number)

    ele3 = driver.find_element(by=By.XPATH,value="//input[@id='caseYear']")
    ele3.send_keys(case_year) 

    submit = driver.find_element(by=By.XPATH,value="//button[@type='submit']")
    submit.click()

    # step 2 get the data from table
    try:
        wait = WebDriverWait(driver,10)
        table_xpath = "//div[@class='modal-body']//table"  

        wait.until(EC.presence_of_element_located((By.XPATH,table_xpath)))

        table_element = driver.find_element(by=By.XPATH,value=table_xpath)
    except NoSuchElementException:
        return {"error":True,"msg":"data not found chek input or try again later"}    
    # table_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))

    rows = table_element.find_elements(By.TAG_NAME, "tr")
    kyes = [
    "Title",
    "Diary number",
    "Location",
    "Case type",
    "Case number",
    "Date of filing",
    ]
    data = {}
    i = 0
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            if i< len(kyes):
              data[kyes[i]] = cell.text.replace("\n", " ")
            i += 1
            print(cell.text)
    print(data)        
    driver.close()
    return {"error":False, "msg":"success", "data":data}
# print(selenium_code("Original Application","100","2016"))    