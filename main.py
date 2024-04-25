import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
diretorio = 'Links dos Materiais'

driver.get('https://www.tcm.pa.gov.br/mural-de-licitacoes/')

for i in range(1, 11):  # ajeitar para automação de geração automatica de arquivos
    html_content = driver.page_source
    a_tag_elements = driver.find_elements(By.XPATH, "//tr/td/a")
    a_tag_elements = [a.get_attribute('href') for a in a_tag_elements]

    with open(f'bidding_page_{i}.html', 'w', encoding='utf-8') as bidding_page:
        bidding_page.write(str(driver.page_source))
    print("Arquivo HTML criado com sucesso!")

    for j, a_tag_element in enumerate(a_tag_elements):
        response_html = requests.get(a_tag_element).text

        with open(f'bidding_page_{i}_record_{j+1}.html', 'w', encoding='utf-8') as bidding_page_record:
            bidding_page_record.write(str(response_html))
        print("Arquivo HTML criado com sucesso!")
        time.sleep(.5)

    next_page_button = driver.find_element(By.XPATH, "//ul/li[@class='next']")
    next_page_button_link = next_page_button.find_element(By.XPATH, "//a").get_attribute('href')
    driver.get(next_page_button_link)
    time.sleep(2.5)

time.sleep(5)
