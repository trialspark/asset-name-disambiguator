from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class PubchemService:
    def get_synonym(self, asset_name):
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(options=options)
            driver.get("https://pubchem.ncbi.nlm.nih.gov/")
            search_bar = driver.find_element(By.TAG_NAME, 'input')
            search_bar.click()
            search_bar.send_keys(asset_name)
            search_button = driver.find_element(By.CLASS_NAME, 'main-search-submit')
            search_button.click()
            driver.implicitly_wait(5)
            result_link = driver.find_element(By.CLASS_NAME, 'highlight')
            result_link.click()
            driver.implicitly_wait(5)
            synonym_section = driver.find_element(By.ID, 'Depositor-Supplied-Synonyms')
            synonyms = synonym_section.find_elements(By.TAG_NAME, "li")
            synonyms_list = []
            for item in synonyms:
                synonyms_list.append(item.text)
            driver.quit()
            return synonyms_list

        except NoSuchElementException as e:
            print(f"Compound {asset_name} not found.")
            return []
