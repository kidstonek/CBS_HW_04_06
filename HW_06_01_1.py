'''
Завдання 1
Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database,
використовуючи стандартну бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp. Кроки,
які мають бути залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200.
Перевірте хід виконання програми на >3 ресурсах і перегляньте послідовність запису логів в обох варіантах і
порівняйте результати.
Для двох видів завдань використовуйте різні файли для логування, щоби порівняти отриманий результат.
'''

import logging
import requests

resources = [
    'https://api.macvendors.com/',
    'https://pypi.org/',
    'https://www.youtube.com/'
]


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename='mylog_1.log',
    filemode="w",
    datefmt='%Y-%m-%d %H:%M:%S',
    format="%(module)s, %(asctime)s, %(message)s"
)


def main():
    for url in resources:
        logger.info(f'site {url}')
        res = requests.get(url)
        logger.info(f'site {url} with status code: {res.status_code}')


if __name__ == '__main__':
    main()