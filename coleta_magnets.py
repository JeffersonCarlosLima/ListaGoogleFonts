import requests
from bs4 import BeautifulSoup

# URL base do site
base_url = 'https://limontorrents.com/arcane-2a-temporada/'

# Lista para armazenar os links de torrent
torrent_links = []

def get_movie_links(base_url):
    """Coleta os links de filmes na página inicial (movies-list)."""
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar todas as divs 'item' dentro de 'movies-list' e coletar o primeiro <a> de cada
        movie_items = soup.find_all('div', class_='item')
        links = [item.find('a')['href'] for item in movie_items if item.find('a')]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL base: {e}")
        return []

def get_torrent_links_from_page(url):
    """Acessa a página do filme e coleta os links de torrent na div 'links-down'."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Localizar a div 'links-down'
        links_down = soup.find('div', class_='links-down')
        if not links_down:
            print(f"'links-down' não encontrada em {url}")
            return []
        import time
        time.sleep(2)  # Aguarda 2 segundos antes de cada requisição

        # Coletar todos os links magnet ou outros disponíveis dentro de 'links-down'
        torrents = [a['href'] for a in links_down.find_all('a', href=True) if a['href'].startswith('magnet:?')]
        return torrents

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página {url}: {e}")
        return []

# Coleta inicial de links de filmes
movie_links = get_movie_links(base_url)

# Acessa cada link de filme e coleta torrents
for movie_link in movie_links:
    print(f"Acessando página do filme: {movie_link}")
    torrents = get_torrent_links_from_page(movie_link)
    torrent_links.extend(torrents)

# Remove duplicatas e salva os links de torrent
torrent_links = list(set(torrent_links))

with open('torrent_links.txt', 'w', encoding='utf-8') as file:
    for link in torrent_links:
        file.write(link + '\n')

print(f"Coleta finalizada! {len(torrent_links)} links de torrent encontrados e salvos em 'torrent_links.txt'.")
