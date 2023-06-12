import pandas as pd
try:
    table_BB = pd.read_html('Bangladesh Bank.html')
    df = table_BB[0]
    
    df.to_csv('BB_MFS summary statement.csv', index = False)
except Exception as e:
    print(e)