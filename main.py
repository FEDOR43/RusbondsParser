from bs4 import BeautifulSoup
import requests


def get_info():
    site = 'https://old.rusbonds.ru'
    url_bonds = '/compare.asp'
    url = f'{site}{url_bonds}'
    column_names = [
        'Облигация, выпуск',
        'Дата погаш.',
        'Дата оферты.',
        'Дюрац. дней',
        'Купон р/год',
        'Купон % год',
        'Купон НКД',
        'Цена, % ном. чист.',
        'Цена, % ном. изм.',
        'Цена, % ном. грязн.',
        'Дох-ть эфф., % год. погаш.',
        'Дох-ть эфф., % год. изм.',
        'Дох-ть эфф., % год. оферт.',
        'Торги за неделю сдел.',
        'Торги за неделю объем, млн.',
        'В обращении, млн.',
        'Коэф. оборач. х 100%'
    ]
    # bond = 'BCS Structured-33-2025-ев'
    page = requests.get(url)
    page.encoding = 'windows-1251'

    soup = BeautifulSoup(page.text, "lxml")

    tables = soup.find(class_='tbl_data tbl_headgrid')
    result = []
    for table in tables:
        lines = table.find_all('tr')
        for line in lines:
            # print(len(line))
            columns = line.find_all('td')
            for column in columns:
                s = line.text
                # print(len(s))
                if not s.startswith('Облигация') and not s.startswith('р/год') and not s.startswith('* - сделки сегодня'):
                    # print(line.extract().text)
                    result.append(column.text.replace('\xa0', '').strip())



    print(result)



    # links = (soup.findAll(class_='bl'))
    # for link in links:
    #     l = link.get('href')
    #     print(f'{link.text}: {l}')
    # field = soup.find('input', {'class': 'gsm', 'onchange': 'document.frm1.emit.selectedIndex=0'})
    # btn = soup.find('input', {'class': 'btc', 'value': '   найти   '})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
