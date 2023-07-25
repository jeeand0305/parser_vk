import requests
import re
import requests
import lxml
from bs4 import BeautifulSoup as bs
import codecs
import time

# __________вариант нажатия на кнопку при работе с сайтом_
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('http://yo.ur/pretty-and-cool/url')
# element = driver.find_element_by_css_selector('button.with-class#or-id')
# element.click()
# ___________________________________________________



url = "https://vk.com/search?c%5Bage_from%5D=25&c%5Bage_\
to%5D=42&c%5Bcity%5D=56&c%5Bname%5D=1&c%5Bper_page%5D=\
40&c%5Bq%5D=%D0%B0&c%5Bsection%5D=people"

# <div id="search_more_results"><div class="people_row search_row clear_fix" \
# data-id="214391098" data-sec="people"> <div class="img"><a href="/id214391098"\
# onclick="return nav.go(this, event);" class="AvatarRich AvatarRich--sz-80 AvatarRich--shadow" \
# style="width: 80px; height: 80px; border-radius: 50%;
#  --avatar-rich-stroke-width: 3px; --avatar-rich-nft-frame-width: 4px ">


def parser_timer():
    time.sleep(10)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}
    html_2 = requests.get(url, headers=headers)
    html_izmen_headers = html_2.text
    soup_headers = bs(html_izmen_headers, "lxml")
    div_pars = soup_headers.find_all("div", class_="people_row search_row clear_fix")
    print(div_pars)
    print("________________________________________________________________________________________________")

count=0
while count<2:
    parser_timer()
    count+=1


# # на первом урл выяляем extra_url всех команд
# div = soup.find_all\
#     ("div", class_="table-custom-responsive mb-3")[0]
# # table = div.find("table", class_="table-roster")
# # "text-left text-dark font-weight-normal"#, class_="pt-0 pb-0 pr-0 pl-2 text-center")
# # собираем класс в таблице где лежат "href"
# table_td_all = div.find_all("td", class_="text-left")

