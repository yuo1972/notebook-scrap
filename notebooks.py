from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from store import onlinetrade
from bs_store import kns
from dbnb import insert_spec #, notebooks, conn


ONLINETRADE_URL = "https://www.onlinetrade.ru/catalogue/noutbuki-c9/?browse_mode=4&sort=price-asc&per_page=45&page="
ONLINETRADE_PAGE = 5

KNS_URL = 'https://www.knsrostov.ru/catalog/noutbuki/page'
KNS_PREFIX = 'https://www.knsrostov.ru/'
KNS_PAGE = 10


chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# firefox_options = Options()
# firefox_options.set_headless()
# driver = webdriver.Firefox(executable_path='C:/WebDriver/geckodriver.exe', options=firefox_options)
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

for page in range(0, ONLINETRADE_PAGE):
    url = ONLINETRADE_URL + str(page)
    print(url)
    insert_spec(onlinetrade(driver, url))

driver.close()


requests.adapters.DEFAULT_RETRIES = 5

session = requests.Session()
retry = Retry(connect=5, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

for page in range(0, KNS_PAGE):
    url = KNS_URL + str(page+1) + '/'  # kns страницы начинаются с 1
    print(url)
    insert_spec(kns(session, KNS_PREFIX, url))


# conn.close()
