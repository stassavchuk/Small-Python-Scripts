'''This script provides you convenient way to get all phone numbers and locations from sites
list.lviv.ua, list.if.ua etc.

If you are looking for all numbers of some category put the url of it as a first argument.

Eg.

url = http://list.lviv.ua/categories/19/business
get_data(url)

This will provide you data of all pharmacy in Lviv.

'''


import urllib2
from bs4 import BeautifulSoup
import sys


def get_data(url):
    html = urllib2.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find('div', {'class': 'listContainer1'}).find_all('li')

    for idx, link in enumerate(links):
        html = urllib2.urlopen('http://list.lviv.ua' + link.find('a').get('href')).read()
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find('h1', {'itemprop': "name"}).text.replace('\n', '').replace('  ', '')

        print str(idx) + "\t\t" + name

        streets = soup.find_all('div', {'class': 'street'})
        phones = soup.find_all('div', {'class': 'phone'})

        for i, phone in enumerate(phones):
            p = phone.text.replace('\n', '').replace('  ', '')
            if p:
                print str(idx) + "." + str(i) + "\t" + p + "\t\t",
                print streets[i].text.replace('\n', '').replace('  ', '')
        print


def main():
    try:
        url = sys.argv[1]
    except:
        return
    get_data(url)


if __name__ == '__main__':
    main()
