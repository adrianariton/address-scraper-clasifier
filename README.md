# Address scraping from a range of websites
## How to run:

You have two possibilities!
1.  Un paralelized script (quite slow but shows a lot of the thought process i went through). Not reccmended, but highly recommende to go through the code!
```bash
## From ./Task1
flask --app berver.py run
```

Output will be received as test in [output/NER_REC.txt](output/NER_REC.txt), and the intermadiary output will be available on the web page and also in [output/intermediary.txt](output/intermediary.txt)


## 2.  With AddressSpider (a lot faster)

If you want to run in parralel and faster, run 
```bash
scrapy runspider address_spider.py
```
With output in `spider_logs`

## Training and Dataset building
Check out [ner_train](ner_train)

# Thinking Process

First of all the website is parsed and some rough candidates for zipcode, country, county and directions are identified and marked as tokens.

Afterwards a padding is set for each token (meaning for a given token, n words before and m after are brought into its segment). If two segments overlap, they are joined. This is done, for easier training for NER on shorter sentences.

If ran with option 1. the output of this operation can be observed on the main page after loading or in [output/intermediary.txt](output/intermediary.txt).

Afterwards, using the pretrained model (see [ner_train](ner_train)), the wanted tokens are identified!

If ran with 2., the output can be viewed in [spider_logs/ADDRESSES.txt](spider_logs/ADDRESSES.txt)

#