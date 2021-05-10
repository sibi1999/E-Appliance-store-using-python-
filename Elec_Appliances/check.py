import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345sibi",
  database="eapp"
)

mycursor = mydb.cursor()


print("price and product grouping")
sql = "select product,sum(price) from customer_table group by product;"
mycursor.execute(sql)
for i in mycursor:
    print(i)


print()
print("price and date grouping")
sql = "select product,sum(price) from customer_table group by date;"
mycursor.execute(sql)
for i in mycursor:
    print(i)



print()
print("price and city grouping")
sql = "select region,sum(price) from customer_table group by region;"
mycursor.execute(sql)
for i in mycursor:
    print(i)
'''
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
'''
