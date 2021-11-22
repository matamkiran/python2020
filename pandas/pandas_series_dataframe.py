import pandas as pd


df=pd.Series([5,6],index=[0.0,1.2])

print(df)

df_reset=df.reset_index(level=0,drop=True)

print(df_reset)