# Train NER for recognizing bits of addreses

## Generating the dataset
The hardest part of the process is to build the data set. This is dont by scraping a random real address
generator website: [https://www.fakepersongenerator.com/random-address?new=refresh](https://www.fakepersongenerator.com/random-address?new=refresh)

The output will be written into [data2.py](data2.py), in python. This can then be copied in a newly created gen# file located in [data_logs](data_logs),
and used for training!

To build dataset:
```bash
python3 data_scrape.py
```

## Training the model, and testing
The NER training is performed using **scrapy**, and the affermentioned dataset. Although the model is not 100% accurate, it works 90 percent of the time. After training a new model will be creared in the [trained](trained) folder.

To train model:
```bash
python3 ner_train.py
```

[ ] Modify lines 9-10 in `ner_train.py` to use new models if necesarry:
```python
... # ner_train.py
9 | from data_logs.sentences2 import TRAINING_DATA2 as TRAIN_DATA_SEN
10| from data_logs.gen3 import TRAINING_DATA2 as TRAIN_DATA
...
```
