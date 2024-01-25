from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

import requests
import urllib.parse


class PubchemService:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)

    def get_synonym(self, asset_name):
        try:
            self.search_for_asset(asset_name)
            synonym_section = self.driver.find_element(By.ID, 'Depositor-Supplied-Synonyms')
            synonyms = synonym_section.find_elements(By.TAG_NAME, "li")
            synonyms_list = []
            for item in synonyms:
                synonyms_list.append(item.text)
            self.driver.quit()
            return synonyms_list

        except NoSuchElementException:
            print(f"Compound {asset_name} not found.")
            return []

    def get_compound_and_brands(self, asset_name):
        try:
            self.search_for_asset(asset_name)
            compound_name = self.driver.find_element(By.TAG_NAME, "h1").text
            brand_names = self.get_fda_approved_drugs(compound_name)
            return {'compound_name': compound_name, 'brand_names': list(brand_names)}
        except NoSuchElementException:
            print(f"Compound {asset_name} not found.")
            return {'compound_name': None, 'brand_names': []}
        pass

    def get_fda_approved_drugs(self, compound_name):
        response = requests.get(f'https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:"{urllib.parse.quote_plus(compound_name)}"&limit=1000').json()
        brand_names = set()
        if 'results' not in response:
            print(f'no brand names found for {compound_name}')
            return []
        for result in response['results']:
            for product in result['products']:
                brand_names.add(product['brand_name'])

        return brand_names

    def search_for_asset(self, asset_name):
        self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")
        search_bar = self.driver.find_element(By.TAG_NAME, 'input')
        search_bar.click()
        search_bar.send_keys(asset_name)
        search_button = self.driver.find_element(By.CLASS_NAME, 'main-search-submit')
        search_button.click()
        self.driver.implicitly_wait(5)
        result_link = self.driver.find_element(By.XPATH, "//a[contains(@data-action,'featured-result-link')]")
        result_link.click()
        self.driver.implicitly_wait(5)
