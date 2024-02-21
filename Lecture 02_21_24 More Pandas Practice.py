#Lecture 02/21/24 More Pandas Practice
import pandas as pd 
df = pd.read_csv('big-mac-full-index.csv')
# Setting up the queriers 
    # country = "Brazil"
    # query_text = f"name == '{country}' & 'dollar_price < 2' "
    # df_query = df.query(query_text)
    # print(df_query)

# Using a year to filter the data 
    # year = 2020
    # query_text = f"date > '2020-01-01' & date < '2020-12-31'"
    # df_year= df.query(query_text)
    # print(df_year)

#
year = "2020"
query_text =  f'date> {year}-01-01'

df_results = df.query(query_text)

