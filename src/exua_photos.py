'''
Script that downloads all photos from EX.UA that specified in urls.txt.

urls.txt could contain something like this:
http://www.ex.ua/get/236614675
http://www.ex.ua/get/236615334
http://www.ex.ua/get/236615584
...

'''


import urllib
from tqdm import tqdm

f_name = './urls.txt'
download_place = './pics/'


def main():
    with open(f_name, 'r') as f:
        links = f.read().split('\n')

    zf = len(str(len(links)))

    for idx, link in enumerate(tqdm(links)):
        urllib.urlretrieve(link, download_place + str(idx).zfill(zf) + '.jpg')


if __name__ == '__main__':
    main()
