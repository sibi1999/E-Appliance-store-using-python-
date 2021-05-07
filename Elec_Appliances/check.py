from collections import Counter
import json
def counting_function(x):
    d=json.loads(x)
    print(d)
    print(Counter(d))
    print(d.values())
    return 0
    
import pandas as pd

df = pd.DataFrame(pd.read_csv('data.csv'))
print(df)
#df["quantity"]=df["product"].apply(counting_function)
print(df.groupby('region').sum())
print(df.groupby('date').sum())

print()
print()
print(json.loads(df['product']))

