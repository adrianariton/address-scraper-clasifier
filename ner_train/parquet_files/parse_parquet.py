import pandas as pd


parquet_urls = pd.read_parquet('dataset.parquet', engine='pyarrow')
limit = 30
for url in parquet_urls.iterrows():
    limit -= 1
    if limit == 0:
        break
    a, b = url
    print(b, f"\n{limit}\n-----\n\n")