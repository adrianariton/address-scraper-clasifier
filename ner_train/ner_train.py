from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from spacy.training.example import Example
from tqdm import tqdm

from data_logs.sentences2 import TRAINING_DATA2 as TRAIN_DATA_SEN
from data_logs.gen4 import TRAINING_DATA2 as TRAIN_DATA
from data import ALL_TRAINING_DATA

TRAIN_DATA = TRAIN_DATA + TRAIN_DATA_SEN

TEST_DATA = [
    ('60195 Glendale Heights Location 2021 Bloomingdale Rd Glendale Heights', {}),
    ('With Us Physical Address​ 503 Maurice Street Monroe NC 28112 Phone Numbers 1-704-283-6342', {}),
    ('Leadership Training Contact Info 503 Maurice Street Monroe NC 28112 +1 704-283-6342 embcmonroe', {}),
    ('columbus, ohio 43230', {})
]


model = None
output_dir=Path("./")
n_iter=100

# load the model

if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")


if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe('ner')
    
    
for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)

            nlp.update(
                [example],  
                drop=0.5,  
                sgd=optimizer,
                losses=losses)
        print(losses)

# output directory       
nlp.to_disk('./trained/')
for text, _ in TEST_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])