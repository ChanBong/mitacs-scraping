from selenium.webdriver.common.by import By
from selenium import webdriver
import time 
import pandas as pd

PROJECT_PAGE = 'https://globalink.mitacs.ca/#/student/application/projects'
TOTAL_PAGES = 297

driver = webdriver.Chrome()
driver.get('https://globalink.mitacs.ca/#/student/application/projects')
print("Page loaded...")

time.sleep(5) # Wait for the page to load completely

def SinglePageScrape():
    elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'col-12') and contains(@class, 'col-md-12') and contains(@class, 'ng-star-inserted')]")

    for element in elements:
        id_name = element.find_elements(By.CLASS_NAME, 'row')

        try:
            project_id = id_name[0].text.split('\n')[0].split()[-1]
            print(f"Writing project id: {project_id}")
        except:
            continue

        try:
            description = id_name[1].text
            details = description.split('\n')

            project_name = details[0]
            project_description = details[1]
            prof = details[2].split(':')[-1].strip().replace(',', ';')
            host_province = details[3].split(':')[-1].strip().replace(',', ';')
            host_univ = details[4].split(':')[-1].strip().replace(',', ';')
            host_campus = details[5].split(':')[-1].strip().replace(',', ';')
            location = details[6].split(':')[-1].strip().replace(',', ';')
            language = details[7].split(':')[-1].strip().replace(',', ';')
            start_date = details[8].split(':')[-1].strip().split('(')[0].strip().replace(',', ';')

            df.loc[len(df)] = [project_id, project_name, project_description, prof, host_province, host_univ, host_campus, location, language, start_date]
        except:
            pass

    # Turn page
    elements = driver.find_element(By.XPATH, '//button[@class="p-ripple p-element p-paginator-next p-paginator-element p-link"][1]')
    driver.execute_script("arguments[0].click();", elements)

date = time.strftime("%Y%m%d")
excel_file = f'results/mitcas_projects24_till_{date}.xlsx'

df = pd.DataFrame(columns=['Project ID', 'Name', 'Description', 'Faculty supervisor', 'Host Province', 'Host Institution', 'Host Campus', 'Location', 'Language', 'Preferred start date'])

for page in range(TOTAL_PAGES):
    print(f"On page {page + 1} of {TOTAL_PAGES}")
    time.sleep(3) # Wait for the page to load completely
    SinglePageScrape()

df.to_excel(excel_file, index=False)