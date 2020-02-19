import requests
import json
from bs4 import BeautifulSoup

url = 'https://free-proxy-list.net/'


def main():
    response = requests.get(url)
    ip_list = []
    if response.status_code == 200:
        html = BeautifulSoup(response.content, 'html.parser')
        table = html.find('table', class_='table')
        rows = table.find_all('tr')
        for row in rows:
            data, ob = row.find_all('td'), {}
            for i in range(len(data)):
                if i == 0:
                    ob['ip'] = data[i].text
                if i == 1:
                    ob['port'] = data[i].text
                if i == 2:
                    ob['country'] = data[i].text
            if ob:
                ip_list.append(ob)

    with open('ip.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps({'items': ip_list}, indent=4))


if __name__ == '__main__':
    main()
