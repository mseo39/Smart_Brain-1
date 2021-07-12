import pandas as pd

f = pd.read_csv('CWA-DATA.csv')

df = pd.DataFrame(f)

df.columns = ['Date','X_axis','Y_axis','Z_axis','X','Y','Z']

print(df)