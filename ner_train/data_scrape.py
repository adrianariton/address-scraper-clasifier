'''
    Data software script.
    
    How it works?
    
    Make requests to https://www.fakepersongenerator.com/random-address?new=refresh,
    and process the output as neede using the config variable
    
        | config = ['SHORT'] -- sh#.py               -- no street
        | config = [] -- gen#.py                     -- all
        | config = ['CUT', 'STREET_ZIP'] -- cush#.py -- street and zip with shorcut
        |                                               (street -> st.)
        | etc

    Run from base folder:
    
        | python3 ner_train/data_scrape.py
    
    Output will be generated in `data2.py`, an can be copied in the data_logs folder
'''


from bs4 import BeautifulSoup, SoupStrainer
import re
from flask import Flask
from flask import request
import requests
from urllib.request import Request, urlopen, urlcleanup
import urllib
import multiprocessing
import geograpy
import pandas as pd
import nltk
import numpy
import time
from selenium import webdriver
from requests_html import HTMLSession
from random import randint
session = HTMLSession()

# config = ['SHORT'] -- sh#.py
# config = [] -- gen#.py
config = ['CUT', 'STREET_ZIP']

random_words = [
    'with', 'at', 'by', 'to', 'in', 'for', 'from', 'of', 'on',
    "free",
    "estimate",
    "We",
    "USE",
    "with",
    "address",
    "in",
    "that",
    "Phone",
    "Number",
    "phone",
    "number",
    "location",
    "contact",
    "information",
    "Contact Information",
    "Contact",
    "Information"
]

INSERT_RANDOM_WORDS = True


def scrape_page(url):
    print ("URL: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = numpy.random.permutation(len(a))
    return a[p], b[p]

def generate_addresses(perms, file, remove_not_needed=False):
    
    '''
        This function is used to generate the dataset, from a random generator
    '''
    
    url = 'https://www.fakepersongenerator.com/random-address?new=refresh'
    
    if url == None or len(url) == 0:
        return []
    urlcleanup()  

    #req = Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15')
                   
    #req.add_header('Referer', 'https://www.fakepersongenerator.com')
    
    #webpage = urlopen(req)
    #time.sleep(.1)
    #webpage = webpage.read()
    session = HTMLSession()
    r = session.get(url, headers={'Referer' : 'https://www.fakepersongenerator.com/',
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'})
    time.sleep(0.1)
    r.html.render() 
    #soup = BeautifulSoup(r.html, 'html.parser')
    
    titles = r.html.find(".info-title")
    vals = r.html.find(".info-detail")
    #print(titles, vals)
    i = 0
    names = []
    props = []
    
    intro = randint(0, 20)
    idx = randint(0, len(random_words)-1)
    
    for el in titles:
        #print(el)
        type = el.find("span")
        out = vals[i].find('input')
        
        if INSERT_RANDOM_WORDS:
            if True:
                if i == intro/2:
                    props += ["OTHER"]
                    names += [random_words[idx]]
                    idx = randint(0, len(random_words)-1)

        
        type = u''.join(type[0].text)
        type = type.upper()
        
        if remove_not_needed:
            # print(f"TYPE: {type}")
            if type in ['TIMEZONE', 'LATITUDE', 'LONGITUDE', 'MOBILE NUMBER', 'TELEPHONE NUMBER']:
                i+=1
                continue
        if 'SHORT' in config:
            if type in ['STREET ADDRESS', 'ZIPCODE']:
                i+=1
                continue
            
        if 'STREET_ZIP' in config:
            if type not in ['STREET ADDRESS', 'ZIPCODE']:
                i+=1
                continue
            
            
            
        out = out[0].attrs['value']
        if 'CUT' in config:
            out = out.lower().replace('road', 'rd.')
            out = out.lower().replace('street', 'st.')
            out = out.lower().replace('terrace', 'bvd.')
            out = out.lower().replace('lane', 'bvd.')
            out = out.lower().replace('drive', 'dr.')



        type = type.replace(' ', '_')
        print(type, out)
        
        props = props + [type]
        names = names + [out]
        
        i += 1
    
    if (len(names) == 0):
        return -1
    
    print(props, names)
    
    for i in range(perms):
        # props, names = unison_shuffled_copies(numpy.array(props), numpy.array(names))
        str = ' '.join(names)
        l = 0
        i = 0
        print('(', file=file)
        print(f'"{str.strip()}"', file=file)
        print(', {\n"entities":[', file=file)
        for a in names:
            g = l + len(a)
            

            if props[i] != 'OTHER' or not INSERT_RANDOM_WORDS:
                print(f'({l}, {g}, "{props[i]}"),', file=file)
            
            l += len(a)
            l += 1 #space
            i += 1
        print(']\n}),', file=file)
    session.close()  
    urlcleanup()  
    return 0
    #req.close()
    
f = open('ner_train/data2.py', 'w') 
print('TRAINING_DATA2 = [', file=f) 

for i in range(100):
    x = generate_addresses(perms=1, file=f, remove_not_needed=True)
    if x == -1:
        print('Skipped verif, sleeping for 10 secs')
        time.sleep(10)
        print('done!')
    urlcleanup()

print(']', file=f)