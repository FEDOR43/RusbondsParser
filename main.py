from bs4 import BeautifulSoup
import requests


def get_info():
    site = 'https://old.rusbonds.ru'
    url_bonds = '/compare.asp'
    url = f'{site}{url_bonds}'
    column_names_eng = [
        'Bond',
        'Payment date',
        'Offer date',
        'Macaulay duration, days:',
        'Coupon rub/year',
        'Coupon % per year',
        'Coupon NKD',
        'Price, % nominal clean',
        'Price, % nominal rev.',
        'Price, % nominal dirty',
        'Effective yield, % annual repayment',
        'Effective yield, % annual change',
        'Effective yield, % annual offer',
        'Trades for the week, trades',
        'Weekly trading volume, millions',
        'In circulation, millions',
        'Turnover ratio x 100%',
    ]
    column_names_rus = [
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

    page = requests.get(url)
    page.encoding = 'windows-1251'

    soup = BeautifulSoup(page.text, "lxml")

    table = soup.find(class_='tbl_data tbl_headgrid')
    result_tmp = []
    result_list = []
    for element in table:
        lines = element.find_all('tr')
        for line in lines:
            columns = line.find_all('td')
            for column in columns:
                s = line.text
                if not s.startswith('Облигация')\
                        and not s.startswith('р/год')\
                        and not s.startswith('* - сделки сегодня'):
                    result_tmp.append(column.text.replace('\xa0', '').strip())
                if result_tmp != []:
                    result_list.append(result_tmp)
            result_tmp = []

    all_bonds = {}
    for bond in result_list:
        tmp = {}
        for i in range(len(bond)):
            entry = {
                column_names_eng[i]: bond[i]
            }
            tmp.update(entry)
        obl = {bond[0]: tmp}
        all_bonds.update(obl)

    print(all_bonds)
    print(all_bonds.get('BCS Structured-10-2022-ев').get('Payment date'))

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
