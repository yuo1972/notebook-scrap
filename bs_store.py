from bs4 import BeautifulSoup
import re

from util import get_rank


def get_price(str0):
    match = re.search('\d+', str0.replace('\xa0', ''))
    return int(match[0]) if match else 0


def get_spec(str0):
    ghz = 0
    ram_gb = 0
    inch = 0
    ssd_gb = 0

    lst = str0.split(', ')
    for spec in lst:
        if 'GHz' in spec:
            match = re.search('([\d\.]+) GHz', spec)
            if match:
                ghz = float(match[1])
        if 'Mb' in spec:
            if re.search('^\d', spec):    # ОЗУ начинается с цифры, в отличие от видео-ОЗУ
                ram_gb = int(re.sub('\D', '', spec)) // 1024
        if 'Gb SSD' in spec:
            match = re.search('(\d+) Gb SSD', str0)
            ssd_gb = int(match[1]) if match else 0
        if '"' in spec:
            match = re.search('([\d\.]+)"', spec)
            if match:
                inch = float(match[1])

    return (ghz, ram_gb, inch, ssd_gb)


def kns(session, prefix, url):
    resp = session.get(url)

    knsnotebook = BeautifulSoup(resp.text, 'html.parser')
    notebooks = knsnotebook('div', class_='goods-list-item mx-auto')

    list2db = []
    if len(notebooks):
        for nbook in notebooks:
            # print(nbook)
            specification = {}

            specification['name'] = nbook.find(itemprop='name').text
            specification['url'] = prefix + nbook.find(class_='name').attrs['href']
            specification['price_rub'] = get_price(nbook.find(class_='price').text)

            (specification['cpu_hhz'], specification['ram_gb'], specification['disp_inch'], specification['ssd_gb']) = \
                get_spec(nbook.find(class_='goods-annt').text)

            specification['rank'] = get_rank(specification['cpu_hhz'], specification['ram_gb'], specification['ssd_gb'],
                                             specification['disp_inch'], specification['price_rub'])

            print(specification)
            list2db.append(specification)
            # break

    return list2db