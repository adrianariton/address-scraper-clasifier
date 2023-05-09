# Address scraping from a range of websites
## How to run:
```bash
## From ./Task1
flask --app berver.py run
```

Output will be received as test in [output/NER_REC.txt](output/NER_REC.txt), and the intermadiary output will be available on the web page and also in [output/intermediary.txt](output/intermediary.txt)

## Training and Dataset building
Check out [ner_train](ner_train)

# Thinking Process

First of all the website is parsed and some rough candidates for zipcode, country, county and directions are identified and marked as tokens.

Afterwards a padding is set for each token (meaning for a given token, n words before and m after are brought into its segment). If two segments overlap, they are joined. This is done, for easier training for NER on shorter "sentences".

The output of this peration can be observed on the main page after loading or in [output/intermediary.txt](output/intermediary.txt).

Afterwards, using the pretrained model (see [ner_train](ner_train)), the wanted tokens are identified!