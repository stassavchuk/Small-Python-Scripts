'''This script aimed to provide you total time of YouTube playlist.
Put the url of list as a first argument.
Eg. https://www.youtube.com/playlist?list=PLMdDrIM5JRUmeLIRd3P0AFo3D-AYw4xEj
'''


from bs4 import BeautifulSoup
import urllib
import sys


def get_time(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    times = soup.find_all('div', {'class': 'timestamp'})
    mm = 0
    ss = 0
    for time in times:
        m, s = time.text.split(':')
        mm += int(m)
        ss += int(s)

    mm += ss // 60
    ss %= 60
    hh = mm // 60
    mm %= 60
    return '%i:%i:%i' % (hh, mm, ss)


def main():
    try:
        url = sys.argv[1]
        print get_time(url)
    except:
        pass

if __name__ == '__main__':
    main()
