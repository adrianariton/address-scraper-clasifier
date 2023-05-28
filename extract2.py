from bs4 import BeautifulSoup, SoupStrainer
import re
from flask import Flask
from flask import request
import requests
from urllib.request import Request, urlopen
import multiprocessing
import geograpy
import pandas as pd
import nltk
nltk.download('punkt')

def scrape_page(url):
    '''
        Testing function for webscraping (unused)
    '''
    print ("URL: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    # get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print ("Done")

def parse_countries():
    '''
        A list of countries
    '''
    return open("countries.txt", "r")

def parse_states():
    '''
        A list of US states
    '''
    keys = []
    for line in open('states.csv', 'r'):
        keys += [line.split(',')[0].strip().upper(), line.split(',')[1].strip().upper()]
        keys += [line.split(',')[0].strip(), line.split(',')[1].strip()]
    return keys

def parse_suffixes():
    '''
        Returns the suffixes that usualy appear in addreses
    '''
    return ['st', 'street', 'bvd', 'boulevard', 'ave', 'avenue', 'rd', 'road', 'st.', 'rd.', 'bvd.', 'ave.']

def parse_directions():
    '''
        Directions (N, S, E ,V) and others
    '''
    return ['north', 'south', 'west', 'east', 'N', 'S', 'E', 'W', 'n', 'e', 'v']

def bad_token(tok):
    '''
        This function cheks if token is not text
            ergo line of code.
    '''
    if tok == '\n' or tok == ' ':
        return 1
    bad = ":({;"
    for el in bad:
        if el in tok:
            return 1
    return 0

def clean_token(tok):
    '''
        This function cleans token off double spaces and/or tabs
    '''
    tok = tok.replace('\t', ' ')
    result = " ".join(tok.split())
    return result

punctuation = ['.', ' ', '?', '!', ',']

def contains_keywds(tok, wds):
    for wd in wds:
        for p in punctuation:
            for q in punctuation:
                if f"{p}{wd}{q}" in tok:
                    return 1
    return 0

def contains_str(tok, wds):
    for wd in wds:
        if f"{wd}" in tok:
            return 1
    return 0

def matches_regex(tok, rgx_str):
    pattern = re.compile(rgx_str)
    match = pattern.search(tok)
    if match:
        return 1
    return 0

def matches_config_keywds(tok):
    keys = ['street', 'st', 'rd', 'bvd']
    return contains_keywds(tok, keys)

def matches_postal_code_US(tok):
    pattern = r"\b\d{5}\b"
    return matches_regex(tok, pattern)

def matches_countries(tok):
    keys = parse_countries()
    keys = [i.strip().lower() for i in keys]
    return contains_keywds(tok, keys)

def matches_US_states(tok):
    keys = []
    for line in open('states.csv', 'r'):
        keys += [line.split(',')[0].strip().lower(), line.split(',')[1].strip().lower()]
    return contains_keywds(tok, keys)

def filtering_function(tok):
    return matches_postal_code_US(tok) or matches_config_keywds(tok) or matches_countries(tok)

def is_url_to_file(url):
    return contains_str(url, ['.pdf', '.png', '.jpg', '.jpeg', '.txt', '.css'])


def parsing_functions_addresses(soup):
    tokens = soup.find_all(text=True)
    
    # throw away css code and things that can be estimated as code
    tokens_filtered = [i for i in tokens if not bad_token(i)]
    
    # clean tokens of multiple tabs and/or spaces
    tokens_cleaned = [clean_token(i) for i in tokens_filtered]
    new_tokens = [i.lower() for i in tokens_cleaned]
    
    # print tokens that have keywords
    keyed_tokens = [i for i in new_tokens if filtering_function(i)]
    return keyed_tokens

def strict_segment_positions(pos, toks):
    '''
        This function returns the nearest segment positions 
        of a token according to the following rules:
            suffixes: 6 before, 2 after
            countries, directions: 2 before, 2 after
            states: 2 before, 4 after
    '''
    if not (pos < len(toks) and pos >= 0):
        return (0, 0)
    
    if toks[pos].lower().strip() in parse_suffixes():
        return (6,2)
    if toks[pos].strip() in parse_countries():
        return (2,2)
    if toks[pos].strip() in parse_states():
        return (2,4)
    if toks[pos].strip().lower() in parse_directions():
        return (2,2)
    return (0,0)

def segment_pos(pos, toks):
    '''
        This function joins overlapping segments
        of a given token.
        The segments will be used for NER after cleaning
        by function segment and _Segment
    '''
    i = pos
    m, n = strict_segment_positions(pos, toks)
    m = pos - m
    n = pos + n
    
    while i >= m:
        _m, _n = strict_segment_positions(i, toks)
        m = min(m, i - _m)
        n = max(n, i + _n)
        if _m == 0 and i == m:
            break
        i -= 1
        
    i = pos
    
    while i <= n:
        _m, _n = strict_segment_positions(i, toks)
        m = min(m, i - _m)
        n = max(n, i + _n)
        if _n == 0 and i == n:
            break
        i += 1
        
    return pos - m, n - pos

def _segment(pos, m, n, toks):
    '''
        Segment to string
    '''
    i = pos - m
    i = max(0, i)
    ans = ''
    while i <= min(pos + n, len(toks) - 1):
        ## if i == pos:
        ##    ans += f' **[-{m}][{n}]'
        ans += f'{toks[i]} '
        i+=1
    return ans.strip()

def segment(pos, toks):
    '''
        This function returns the nearest segment positions 
        of a token according to the following rules:
            suffixes: 6 before, 2 after
            countries, directions: 2 before, 2 after
            states: 2 before, 4 after
        it joins overlaping segments and returns the tokens
        joined in a string if existent.
    '''
    m, n = segment_pos(pos, toks)
    if m == 0 and n == 0:
        return ''
    return _segment(pos, m, n, toks)     

def new_parsing_fct(soup):
    tokens = soup.find_all(text=True)
    tokens_filtered = [i for i in tokens if not bad_token(i)]
    
    # clean tokens of multiple tabs and/or spaces
    tokens_cleaned = [clean_token(i) for i in tokens_filtered]
    
    # join tokens
    tok_str = ' '.join(tokens_cleaned)
    
    toks = nltk.word_tokenize(tok_str)
    toks = [i for i in toks if i not in ",.?!:;-&``~/#$%^*⬤"]
    
    segm1 = [segment(position, toks) for position, i in enumerate(toks)]
    segm1 = [i for i in segm1 if len(i.strip()) > 0]
    return segm1


depth = 1
def ex(url, first=0, parsed_next_links=[], base="", max_iter = 3, parsing_fct=parsing_functions_addresses):
    '''
        Reccursive (quite slow) function that reccursively scrapes a page
        then it's linked pages to return near-address strings (segments).
        
        For better performance, use address_spider.py (view README.md)
    '''
    
    x = (url.split('/'))
    x = [i for i in x if i != None and len(i) > 0]
    if max_iter < 0:
        return []
    url = "/".join(x)
    url= url.replace(":/", "://")
    print(f"Rep #{max_iter}: {url}")
    
    if (is_url_to_file(url)):
        print("\t-[skipped] Url is path to non html file.")
        return []
    
    if url == None or len(url) == 0:
        return []
    try:
        req = Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15')
        webpage = urlopen(req).read()
    except:
        print(f"Could not open {url}")
        return []
    print(f"Opening: {url}")
    
    # With geograpy:
    # places = geograpy.get_geoPlace_context(url=url)    
    # print(f"\t\t- With geograpy: {places}")
    
    parsed_next_links += [url]

    if first == 1:
        max_iter = 3
        base = url
        parsed_next_links = [url]
        
    try:
        soup = BeautifulSoup(webpage, 'html.parser')
    except:
        print(f"Non-utf chars found [perhaps] as/in {url}")
        return []
    # decrease number of remaining links
    max_iter -= 1

    keyed_tokens = parsing_fct(soup=soup)
    print(keyed_tokens)

    # return keyed_tokens

    if depth == 0:
        return keyed_tokens
    # scrape next page (linked in a) if exists
    
    # create a list of all next pages
    next_links = []
    for link in BeautifulSoup(webpage, 'html.parser', parse_only=SoupStrainer('a')):
        next_links += [link]

    '''
        Crawl link
    '''
    for link in next_links:
        if link.has_attr('href'):
            #print(link['href'])
            href = link.get("href")
            if href in parsed_next_links:
                pass
            else:
                parsed_next_links += [href, f'{url}/{href}', f'{url}{href}']
                if href != None and len(str(href)) > 0:
                    if 'http' not in href and href[0] != '#':
                        print(f"\tInside link to: {href}")

                        # ex(href, parsed_next_links=parsed_next_links)
                        y = ex(f'{base}/{href}', parsed_next_links=parsed_next_links, base=base, max_iter=max_iter, parsing_fct=parsing_fct)
                        #t = ex(f'{base}{href}', parsed_next_links=parsed_next_links, base=base)
                        keyed_tokens += y
                        keyed_tokens = list(set(keyed_tokens))
                    if 'http' in href and base in href:
                        print(f"\tLink to: {href}")

                        y = ex(f'{href}', parsed_next_links=parsed_next_links, base=base, max_iter=max_iter, parsing_fct=parsing_fct)
                        keyed_tokens += y
                        keyed_tokens = list(set(keyed_tokens))

    if first == 1:
        print("{{}}")
        print(keyed_tokens)
        print("[[[[]]]]")
        return keyed_tokens
    return keyed_tokens

def aex(url):
    return ex(url, 1, parsing_fct=new_parsing_fct)

def zips():
    zip_code_regexes = {
        "FIVE":r"\b\d{5}\b",
        "US":r"\b\d{5}([\-]?\d{4})?\b",
        "UK":r"(GIR|[A-Z]\d[A-Z\d]??|[A-Z]{2}\d[A-Z\d]??)[ ]??(\d[A-Z]{2})",
        "DE":r"\b((?:0[1-46-9]\d{3})|(?:[1-357-9]\d{4})|(?:[4][0-24-9]\d{3})|(?:[6][013-9]\d{3}))\b",
        "CA":r"([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ])\ {0,1}(\d[ABCEGHJKLMNPRSTVWXYZ]\d)",
        "FR":r"(F-)?((2[A|B])|[0-9]{2})[0-9]{3}",
        "IT":r"(V-|I-)?[0-9]{5}",
        "AU":r"(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})",
        "NL":r"[1-9][0-9]{3}\s?([a-zA-Z]{2})?",
        "ES":r"([1-9]{2}|[0-9][1-9]|[1-9][0-9])[0-9]{3}",
        "DK":r"([D|d][K|k]( |-))?[1-9]{1}[0-9]{3}",
        "SE":r"(s-|S-){0,1}[0-9]{3}\s?[0-9]{2}",
        "BE":r"[1-9]{1}[0-9]{3}",
        "IN":r"\d{6}",
        "ADDR":r"/\s+(\d{2,5}\s+)(?![a|p]m\b)(([a-zA-Z|\s+]{1,5}){1,2})?([\s|,|.]+)?(([a-zA-Z|\s+]{1,30}){1,4})(court|ct|street|st|drive|dr|lane|ln|road|rd|blvd)([\s|,|.|;]+)?(([a-zA-Z|\s+]{1,30}){1,2})([\s|,|.]+)?\b(AK|AL|AR|AZ|CA|CO|CT|DC|DE|FL|GA|GU|HI|IA|ID|IL|IN|KS|KY|LA|MA|MD|ME|MI|MN|MO|MS|MT|NC|ND|NE|NH|NJ|NM|NV|NY|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VA|VI|VT|WA|WI|WV|WY)([\s|,|.]+)?(\s+\d{5})?([\s|,|.]+)/i"   
    }
    return zip_code_regexes



def run(max_urls, impidx=-1):
    '''
        Run adddress extraction through all the urls of the parquet file (limited
        by max_urls).
    '''
    failed_urls = 0
    address_not_found = 0
    import pandas as pd
    '''
        Parse parquet
    '''
    urls = pd.read_parquet('list.parquet', engine='pyarrow')
    print(urls)
    addresses = []
    i  = max_urls
    j = 0
    for url in urls.iterrows():
        
        if (impidx >= 0 and j != impidx):
            j += 1
            continue
        j += 1
        i -= 1
        if i <= 0:
            break
        print('\n------------------')
        a, b = url
        print(b)
        did = 0
        emp = 0
        nf = 0
        msg = 'a'
        address = aex(f"https://{(b['domain'])}")
        print("^^^^^^^^^")
        print(address)
        print("^^^^^^^^^")
        '''
            Try all combinations of http/https to make sure it works!
        '''
        if address == None:
            continue
        if msg == 'b':
            nf += 1
            addresses.append(['__failed_to_request__'])
        elif len(address) == 0:
            emp += 1
            addresses.append(address)
            did = 1
        else:
            addresses.append(address)
            did = 1
            
        if did == 0:
            address = aex(f"www.{(b['domain'])}")
            if msg == 'b':
                nf += 1
                addresses.append(['__failed_to_request__'])
            elif len(address) == 0:
                emp += 1
                addresses.append(address)
                did = 1
            else:
                addresses.append(address)
                did = 1
        if did == 0:  
            address = aex(f"https://www.{(b['domain'])}")
            if msg == 'b':
                nf += 1
                addresses.append(['__failed_to_request__'])
            elif len(address) == 0:
                emp += 1
                addresses.append(address)
                did = 1
            else:
                addresses.append(address)
                did = 1
        
        if did == 0:  
            address = aex(f"http://{(b['domain'])}")
            if msg == 'b':
                nf += 1
                addresses.append(['__failed_to_request__'])
            elif len(address) == 0:
                emp += 1
                addresses.append(address)
                did = 1
            else:
                addresses.append(address)
                did = 1
        
        if did == 0:  
            address = aex(f"http://www.{(b['domain'])}")
            if msg == 'b':
                nf += 1
                addresses.append(['__failed_to_request__'])
            elif len(address) == 0:
                emp += 1
                addresses.append(address)
                did = 1
            else:
                addresses.append(address)
                did = 1
           
        if did == 0: 
            address = aex(f"{(b['domain'])}")
            if msg == 'b':
                nf += 1
                addresses.append(['__failed_to_request__'])
            elif len(address) == 0:
                emp += 1
                addresses.append(address)
                did = 1
            else:
                addresses.append(address)
                did = 1
                
        if emp > 0:
            address_not_found += 1
        if nf > 0:
            failed_urls += 1
            
    print(f"Failed: {failed_urls}; None found: {address_not_found}")
    return addresses, failed_urls, address_not_found


'''from ner import recognize

def recognize_addresses(addresses):
    for address in addresses:
        record = recognize(address)
        for word in record:
            print(word.text, ' :: ' , word.label_)
'''