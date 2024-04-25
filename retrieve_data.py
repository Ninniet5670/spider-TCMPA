from bs4 import BeautifulSoup
import pandas as pd

# Abra o arquivo HTML
with open('html-data/bidding_page_1_record_1.html', 'r', encoding='utf-8') as file:
    # Leia o conteúdo do arquivo
    html_content = file.read()

# Parseie o HTML com BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Agora você pode extrair informações do arquivo HTML usando os métodos fornecidos pelo BeautifulSoup
# Por exemplo, para encontrar todos os links (<a> tags) no HTML:
tables_html = soup.find_all('table')

dfs = pd.read_html(str(tables_html))

for df in dfs:
    print(df)
    print('\n\n\n\n\n')
