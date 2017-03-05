import os
import shutil

import requests
import click
from bs4 import BeautifulSoup

from unmark import unmark

session = requests.Session()


def fetch_all(keyword, save_dir):
    page = 1
    while 1:
        print('fetch page {}'.format(page))
        if fetch('https://www.iconfinder.com/ajax/search/?page={}&q={}'.format(page, keyword), save_dir) == 200:
           page += 1
        else: 
            break

def fetch(url, save_path):
     """"Fetch all images from a page url"""
     r = session.get(url)
     print('{}'.format(url))
     if r.ok:
        html = r.text
        imgs = BeautifulSoup(html, 'lxml').find_all('img')
        print('{} images'.format(len(imgs)))
        if not imgs: 
            return 400
        for img in imgs:
            src = img['src']
            if src.endswith('.png'):
                filename = os.path.basename(src)
                save(src, os.path.join(save_path, filename))
     return r.status_code
     
def save(src, filename):
    content = session.get(src).content
    with open(filename, 'wb') as f:
        f.write(content)
    try:
        unmark(filename)
        os.remove(filename)
    except:
        pass

@click.command()
@click.argument('keyword')
@click.option('--save-dir', type=click.Path(), default='.')
def cli(keyword, save_dir):
    if not os.path.exists(save_dir): 
       os.mkdir(save_dir)
    fetch_all(keyword, save_dir)

if __name__ == '__main__':
    cli()