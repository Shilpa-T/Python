import pandas as pd
from datetime import datetime
data = pd.read_csv('fruit.log',sep=" ", header = None)
#print data
df_data = pd.DataFrame(data)
#print df_data.head()
data_columns = ['Month','Day','Time','status','path','Fruit','hexcode','Count']
df_data.columns=data_columns

print max(df_data['Time'])
print min(df_data['Time'])