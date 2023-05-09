import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

raw_text="The address is Glendale Heights IL 60139 FREE ESTIMATE 811."
text1= NER(raw_text)

for word in text1.ents:
    print(word.text,word.label_)