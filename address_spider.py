from scrapy import Spider, Request
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup, SoupStrainer
from extract2 import parsing_functions_addresses, new_parsing_fct
import pandas as pd
from ner import recognize_m
from urllib.parse import urlparse

class AddressSpider(Spider):
    '''
        Address Spider scrapes the list of given urls 
        and extracts the addresses similarly to extract2.py, but
        a lot faster.
        
        max_urls is the number of urls from the parquet file it should scrape
        
        Run as such
            | scrapy runspider address_spider.py
    '''
    max_urls = 50
    
    name = 'quote-spdier'
    parquet_urls = pd.read_parquet('list.parquet', engine='pyarrow')
    start_urls = []
    for url in parquet_urls.iterrows():
        max_urls -= 1
        if max_urls == 0:
            break
        a, b = url
        print(b)
        start_urls.append(f"https://{(b['domain'])}")
    print(start_urls, file=open("spider_logs/TEST.txt", 'w'))
    
    depth = 3
    parsing_fct = parsing_functions_addresses
    print('', file=open("spider_logs/ADDRESSES.txt", 'w'))

    def parse(self, response):
        '''
            Parsing function, similar to ex(...) from extract2
        '''
        links = LinkExtractor(allow=()).extract_links(response)
        webpage = response.body

        try:
            soup = BeautifulSoup(webpage, 'html.parser')
        except:
            print(f"Non-utf chars found [perhaps] as/in {url}")
            return []
        
        keyed_tokens = parsing_functions_addresses(soup=soup)
        data = recognize_m(keyed_tokens)
        
        index =  -1
        domain = urlparse(response.url).netloc
        try:
            index = self.start_urls.index(f"https://{domain}")
        except:
            index = "outside"
            
        '''
            Log to log_file
        '''
        print(f"> [{index}] {response.url}", file=open("spider_logs/ADDRESSES.txt", 'a'))
        print(f"\t\ttokenized::recognized")
        for el in data:
            # el = [x for x in el if x[1] != "STATE_FULL"]
            print(f"\t\t{keyed_tokens}::{el}", file=open("spider_logs/ADDRESSES.txt", 'a'))
        print("\n",  file=open("spider_logs/ADDRESSES.txt", 'a'))
        urls = [l.url for l in links]
        self.depth -= 1
        
        
        '''
            Crawl links
        '''
        if self.depth > 0:
            for url in urls:
                yield Request(url, callback=self.parse)
            
            