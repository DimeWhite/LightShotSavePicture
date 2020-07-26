from bs4 import BeautifulSoup as BS
import random
import string
import requests
import re


class LightShot():
    def __init__(self):
        pass

    def create_url(self, chars):
        url = ''
        for i in range(6):
            url+='{}'.format(random.choice(chars))
        return url


    def get_picture(self, url):
        HEADERS ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.197'
        }
        r = requests.get('https://prnt.sc/{}'.format(url), headers=HEADERS)
        html = BS(r.content, 'html.parser')
        image = html.find('img', 'screenshot-image')
        return image['src'], image['image-id']

    def save_picture(self, dir, url, name):
        try:
            r = requests.get(url)
            with open('{}/{}.png'.format(dir, name), 'wb') as imgfile:
                imgfile.write(r.content)
        except:
            pass