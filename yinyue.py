import requests

def requests_music(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def main(page):
    url = 'https://music.163.com/#/discover/toplist'
    html = requests_music(url)