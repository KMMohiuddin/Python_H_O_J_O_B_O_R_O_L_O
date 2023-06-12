import pandas as pd
import os
try:
    existing_df = pd.read_csv('BB_MFS summary statement.csv')
    table_BB = pd.read_html('Bangladesh Bank.html')
    new_df = table_BB[0]
    new_df = new_df.iloc[:,3:4]
    Final_df = pd.concat([existing_df, new_df], axis=1)
    Final_df.to_csv("BB_MFS summary statement.csv", index=False)

except Exception as e:
    print(e)
