import requests
from bs4 import BeautifulSoup

# URL da página do Flutter com os ícones
url = 'https://api.flutter.dev/flutter/material/Icons-class.html'

# Faz a requisição para a página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Faz o parsing do conteúdo da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todos os elementos <dt> com a classe "constant"
    icons = soup.find_all('dt', class_='constant')

    # Extrai e imprime os nomes dos ícones
    icon_names = [icon.find('a').get_text() for icon in icons]

    # Salva os nomes dos ícones em um arquivo
    with open('icon_names.txt', 'w', encoding='utf-8') as file:
        for name in icon_names:
            file.write(f'{name}\n')

    print('Nomes dos ícones foram extraídos e salvos em "icon_names.txt"')
else:
    print('Falha ao acessar a página.')
