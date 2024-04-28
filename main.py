import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
diretorio = 'Links dos Materiais'

driver.get('https://www.tcm.pa.gov.br/mural-de-licitacoes/')

for i in range(1, 11):  # ajeitar para automação de geração automatica de arquivos (itera nas primeiras 10 paginas)
    a_tag_elements = driver.find_elements(By.XPATH, "//tr/td/a")
    a_tag_strong_elements = driver.find_element(By.XPATH, "//tr/td/a/strong")
    a_tag_element_links = [a.get_attribute('href') for a in a_tag_elements]

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    strong_tags = soup.select("tr td a strong")
    a_tag_strong_elements = [str(i).replace('<strong>', '').replace('</strong>', '').strip().replace('/', '.') 
                             for i in list(strong_tags)]


    for j, a_tag_element in enumerate(a_tag_element_links):
        response_html = requests.get(a_tag_element).text

        with open(f'{a_tag_strong_elements[j]}.html', 'w+', encoding='utf-8') as bidding_page_record:
            bidding_page_record.write(str(response_html))
        print("Arquivo HTML criado com sucesso!")
        time.sleep(.5)

    next_page_button = driver.find_element(By.XPATH, "//ul/li[@class='next']")
    next_page_button_link = next_page_button.find_element(By.XPATH, "//a").get_attribute('href')
    driver.get(next_page_button_link)
    time.sleep(2.5)

time.sleep(5)
