from dotenv import load_dotenv
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup

BASE_URL='https://www.sulpak.kz/'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    'g/smartfoniy_apple_iphone_14_plus_256gb_midnight',
    'g/smartfoniy_apple_iphone_14_plus_128gb_midnight'
]

def main(event={}, context={}):
    for item in items:
        url = BASE_URL + item
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        name = soup.select_one('h1[class="title__large product__header-js"]').get_text()
        price = soup.select_one('div[class="product__price"]').get_text()

        data = {
            'chat_id': CHAT_ID,
            'text': f'*{price}*\n[{name}]({url})',
            'parse_mode': 'Markdown'
        }
        r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

if __name__ == '__main__':
    main()