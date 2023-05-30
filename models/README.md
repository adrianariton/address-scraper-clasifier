# Models

v0.1 -> only gen
v0.2 -> gen + sh
v0.3 -> gen + sh + cut 
v0.4? -> v0.3 + (cut + sh)
v0.4.5? -> v0.4 + sen??
v0.5? -> with random words and sentences

# Use

Build dataset, replace with what ge/sh/cut/cush you want and...
```BASH
python3 ner_train.py
```

## Vent:)

I am aware that the models do not excel at predicting when a token is NOT needed for address, and
this can be fixed by creating a model with random senstences found on websites! :)

The models work pretty well though, espectially v.0.3 (models/trained)

## Generated with data_scrape.py 
```python
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
```