# -*- coding: utf-8 -*-
import attr
import scrapy
from bs4 import BeautifulSoup
import requests
import re
from ..items import FacebookItem
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class GoogleSpider(scrapy.Spider):
    name = 'google'
    # allowed_domains = ['google.com']
    #user_query = input('Enter your query: ')

    start_urls = [
         "https://www.google.com/search?q=plumbers+facebook&sxsrf=ALeKk01cY8w_4aH1ji5s3fzFPtdlVl6uww%3A1620182129005&ei=cASSYMHpPMrw9QO_xqDYDg&oq=plumbers+facebook&gs_lcp=Cgdnd3Mtd2l6EAxQAFgAYL3axAJoAHACeACAAcoBiAHKAZIBAzItMZgBAKoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwjB4ZTiwLHwAhVKeH0KHT8jCOsQ4dUDCA4"
    ]

    def parse(self, response):
        df = pd.DataFrame()
        xlink = LinkExtractor()
        link_list=[]
        link_text=[]
        for link in xlink.extract_links(response):
          if len(str(link))>200 or 'Journal' in link.text:
            print(len(str(link)),link.text,link,"\n")
            link_list.append(link)
            link_text.append(link.text)

        for url in link_list:
            link_list.remove("Link(url='https://www.google.com/url?q=", '')
        df['links']=link_list
        df['link_text']=link_text
        df.to_csv('output.csv')


        # for anchor in soup.findall('a'):
        #     print('url', anchor)
        #     link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        #     link = re.sub(r'[.]+[/]', '', link)
        #     #print('url', link)
        #     if 'facebook' in link:
        #         print('urls list', (link))
        #     # if 'google' not in link:
        #     #         print('upstal_mail', link)
        #     #         #email_list.add(upstal_mail)
