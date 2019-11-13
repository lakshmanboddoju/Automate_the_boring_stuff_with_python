#! python3

import bs4, requests

#res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
#res.raise_for_status()

#soup = bs4.BeautifulSoup(res.text, 'html.parser')

#elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')[0]

#elems = elems.text


def getAmazonPrice(productUrl, cssPath):
    res = requests.get(productUrl)
    res.raise_for_status

    soup= bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(cssPath)[0]
    price = elems.text.strip()
    
    return price

retrievedPrice = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/', '#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')

print('The price is ' + retrievedPrice)
