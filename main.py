from bs4 import BeautifulSoup
import requests


def get_info():
    url = 'https://old.rusbonds.ru/compare.asp'
    bond = 'BCS Structured-33-2025-ев'
    # page = requests.get(f'{url}?go=1&tool={bond}')
    page = requests.get(url)
    page.encoding = 'windows-1251'

    soup = BeautifulSoup(page.text, "lxml")

    # tables = soup.find('table', {'class': 'tbl_data.tbl_headgrid'})
    tables = soup.find(class_='tbl_data tbl_headgrid')
    result = []
    for table in tables:
        result += [{table.text: table.next_element.text}]
    print(result)

    # tables = soup.findAll('tbody')
    # for table in tables:
    #     print(table.fetchParents)
    #     print()


    # links = (soup.findAll(class_='bl'))
    # for link in links:
    #     l = link.get('href')
    #     print(f'{link.text}: {l}')
    # field = soup.find('input', {'class': 'gsm', 'onchange': 'document.frm1.emit.selectedIndex=0'})
    # btn = soup.find('input', {'class': 'btc', 'value': '   найти   '})
    # print(field)
    # print(btn)
    # soup2 = BeautifulSoup(field.get(bond), 'lxml')
    # print(soup2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
