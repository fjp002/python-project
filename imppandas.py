#import pandas as pd

#pd.options.display.max_rows = 9999

#df = pd.read_csv('data.csv')

#print(df)


import pandas as py
df = pd.read_json('data.json')

print(df.to_string())
