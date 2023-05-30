from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from spacy.training.example import Example
from tqdm import tqdm

remove = ",/&;!?><\'\"[]{}()"

def out_text_array(text_array, model):
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
    
    for text in text_array:
        for lit in remove:
            text = text.replace(lit, '')
        text = text.lower()
        doc = nlp(text)
        yield [(ent.text, ent.label_) for ent in doc.ents]
        
def recognize_m(text_array):
    return out_text_array(text_array, "./models/trained")


if __name__ == "__main__":
    d = recognize_m(["60195 Glendale Heights Location 2021 Bloomingdale Rd Glendale Heights"])
    for el in d:
        print(el)