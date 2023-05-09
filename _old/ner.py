import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

def recognize(raw_text):
    text1= NER(raw_text)

    for word in text1.ents:
        yield word
        
doc = recognize("Leadership Training Contact Info 503 Maurice Street Monroe NC 28112 +1 704-283-6342 embcmonroe").__doc__
print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
