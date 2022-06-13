from bs4 import BeautifulSoup
import requests


def get_info():
    url = 'https://old.rusbonds.ru/compare.asp'
    bond = 'BCS Structured-33-2025-ев'
    # page = requests.get(f'{url}?go=1&tool={bond}')
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.get_text())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
