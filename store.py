from selenium.webdriver.common.by import By
import re

from util import get_rank


def get_price(str0):
    match = re.search('[\d\s]+', str0)
    return int(match[0].replace(' ', '')) if match else 0


def get_int(str0):
    match = re.search('\d+', str0)
    return int(match[0]) if match else 0


def get_inch(str0):
    match = re.search('[\d.]+', str0)
    return float(match[0]) if match else 0


def onlinetrade(driver, url):
    driver.implicitly_wait(15)
    driver.get(url)

    list2db = []
    notebooks = driver.find_elements(By.CLASS_NAME, "indexGoods__item")
    for nb in notebooks:
        specification = {}

        nb_a = nb.find_element(By.CLASS_NAME, 'indexGoods__item__name')
        specification['url'] = nb_a.get_attribute('href')
        specification['name'] = nb_a.text

        nb_p = nb.find_element(By.CLASS_NAME, 'price')
        specification['price_rub'] = get_price(nb_p.text)

        nb_feature_list = nb.find_elements(By.CLASS_NAME, 'featureList__item')
        spec_tmp = {}
        for nb_f in nb_feature_list:
            if nb_f.text == 'Показать все':
                continue                # сильно тормозит на обработке кнопки 'Показать все'
            nb_f_span = nb_f.find_elements(By.TAG_NAME, 'span')
            if len(nb_f_span) > 1:
                spec_tmp[nb_f_span[0].get_property('innerText')] = nb_f_span[1].get_property('innerText')
                # print(nb_f_span[0].get_property('innerText'), nb_f_span[1].get_property('innerText'))

        specification['cpu_hhz'] = get_int(spec_tmp['Частота CPU:']) / 1024
        specification['ram_gb'] = get_int(spec_tmp['Память:'])
        specification['disp_inch'] = get_inch(spec_tmp['Экран:'])
        if spec_tmp['Диск:'] == 'SSD':
            specification['ssd_gb'] = get_int(spec_tmp['Объем:'])
        else:
            specification['ssd_gb'] = 0

        specification['rank'] = get_rank(specification['cpu_hhz'], specification['ram_gb'], specification['ssd_gb'],
                                         specification['disp_inch'], specification['price_rub'])

        print(specification)
        list2db.append(specification)
        # break

    return list2db