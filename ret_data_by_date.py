import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


day, month, year = map(int, input('Select your date [xx/xx/xxxx]: ').split('/'))

driver = webdriver.Chrome()
diretorio = 'Links dos Materiais'

driver.get(f'https://www.tcm.pa.gov.br/mural-de-licitacoes/?LINCEMVWLICITACOESSearch%5BDATA_PUBLICACAO%5D={day}%2F{month}%2F{year}+-+{day}%2F{month}%2F{year} ')

while True:  # ajeitar para automação de geração automatica de arquivos (itera nas primeiras 10 paginas)
    a_tag_elements = driver.find_elements(By.XPATH, "//tr/td/a")
    a_tag_strong_elements = driver.find_element(By.XPATH, "//tr/td/a/strong")
    a_tag_element_links = [a.get_attribute('href') for a in a_tag_elements]

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    strong_tags = soup.select("tr td a strong")
    a_tag_strong_elements = [str(i).replace('<strong>', '').replace('</strong>', '').strip().replace('/', '.') 
                             for i in list(strong_tags)]


    for j, a_tag_element in enumerate(a_tag_element_links):
        response_html = requests.get(a_tag_element).text
        print(a_tag_element)

        with open(f'html-data/{a_tag_strong_elements[j]}.html', 'w+', encoding='utf-8') as bidding_page_record:
            bidding_page_record.write(f'{a_tag_element}\n{str(response_html)}')
        print("Arquivo HTML criado com sucesso!")
        time.sleep(.5)

    try:
        next_page_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/section/div/div[4]/div/div/ul/li[4]/a").get_attribute('href')
        driver.get(next_page_button)
    except:
        break
    time.sleep(2.5)

time.sleep(5)
