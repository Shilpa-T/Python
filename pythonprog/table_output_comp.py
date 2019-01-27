import pandas as pd

df = pd.read_csv('tableout.txt', sep="\t", header=0)
df_data = pd.DataFrame(df)
print df.head()
print df.shape
#print df.loc[:3,"Delta"]
#print df["Delta"].items()
#print type(df['Delta'].items())

"""
if df.loc[df['Delta'] == str(0)]:
    print 'PASS'
else:
    print 'FAIL'
"""



