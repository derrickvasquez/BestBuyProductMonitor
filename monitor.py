import requests
from bs4 import BeautifulSoup
from discord import send_hook
from datetime import datetime
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

url = 'https://www.bestbuy.com/site/blue-microphones-blue-yeti-professional-multi-pattern-usb-condenser-microphone/4758301.p?skuId=4758301'


headers = {
    'user-agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'user-agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'user-agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'user-agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'user-agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}


print(Fore.MAGENTA+'PREPARING TO MONITOR......')
time.sleep(3)

while True:

    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    atc_button = soup.find('button', attrs={'class': 'add-to-cart-button'}).get_text()
    imageURL = soup.find('img', attrs={'class', 'primary-image'})['src']

    rawPrice = soup.find('div', 'priceView-hero-price').get_text().strip()
    price = rawPrice.split('Your')[0]

    rawSKU = soup.find('div', attrs={'class': 'sku product-data'}).get_text().strip()
    sku = rawSKU.split('SKU:')[1]

    product_title = soup.find('h1', attrs={'class': 'heading-5 v-fw-regular'}).get_text()

    direct_link = 'https://api.bestbuy.com/click/-/' + sku + '/cart'
  
    if atc_button == 'Add to Cart':
        print(Fore.GREEN+ '[{}] PRODUCT IN STOCK'.format(str(datetime.today())))
        send_hook(product_title, url, price, sku, imageURL, direct_link)
    else:
        print(Fore.RED+ '[{}] PRODUCT OUT OF STOCK'.format(str(datetime.today())))
    
