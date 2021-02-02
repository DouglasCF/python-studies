import requests
from bs4 import BeautifulSoup
from datetime import datetime

def check(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()

    print("Title: ", title)
    print("Price: ", price)
    print("Time: ", datetime.now())

check('https://www.amazon.com.br/Cama-Fábrica-Pet-para-Médio/dp/B07ZPC46ZN?ref_=Oct_s9_apbd_omwf_hd_bw_bLS5yTr&pf_rd_r=P1FWTNY7S3FN1R0PPM3S&pf_rd_p=f39f4d6a-13a7-55c9-b267-bbb61c9d9036&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=19653951011')
