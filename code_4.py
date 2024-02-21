import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    pass
    # query_year = df[(df['iso_a3']== country_code.upper()) & (df['date'].str.startswith(str(year)))]
    # rmp_year = round(query_year ['dollar_price'].mean(),2)
    # # print (rmp_year)
    query_year = f'iso_a3 == "{country_code.upper()}" and date > "{year}-01-01" and date < "{year}-12-31"'
    df_year = df.query(query_year)
    rmp_year = round(df_year['dollar_price'].mean(),2)
    return rmp_year

def get_big_mac_price_by_country(country_code):
    pass
    query_country = f'iso_a3 == "{country_code.upper()}"'
    df_country = df.query(query_country)
    rmp_country = round(df_country['dollar_price'].mean(),2)
    # print (rmp_country)
    return rmp_country

def get_the_cheapest_big_mac_price_by_year(year):
    pass
    query_cheapest = df[df['date'].str.startswith(str(year))]
    # filter the dataframe for the specified year
    cheap_row = query_cheapest.loc[query_cheapest['dollar_price'].idxmin()]
    # find the row with the minimum 'dollar_price'
    # .loc goes through the query and finds the lowest price 
    name_of_country = cheap_row['name']
    country_code = cheap_row['iso_a3']
    dollar_price = cheap_row[ 'dollar_price']
    # Extract relevant information from the row 
    # print (f"{name_of_country}({country_code}): ${dollar_price:.2f}")
    return f"{name_of_country}({country_code}): ${dollar_price:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    pass
    query_mexpensive = df[df['date'].str.startswith(str(year))]
    # filter the dataframe for the specified year
    expensive_row = query_mexpensive.loc[query_mexpensive['dollar_price'].idxmax()]
    # find the row with the maximum 'dollar_price'
    # .loc goes through the query and finds the highest price 
    name_of_country = expensive_row['name']
    country_code = expensive_row['iso_a3']
    dollar_price = expensive_row[ 'dollar_price']
    # Extract relevant information from the row 
    # print (f"{name_of_country}({country_code}): ${dollar_price:.2f}")
    return f"{name_of_country}({country_code}): ${dollar_price:.2f}"

if __name__ == "__main__":
    pass
    # print(get_big_mac_price_by_year((input("Enter year: ")), input('Enter country code: ')))
    # print(get_big_mac_price_by_country((input("Enter country code: "))))
    # print(get_the_cheapest_big_mac_price_by_year(input('Enter year: ')))
    print(get_the_most_expensive_big_mac_price_by_year(input('Enter year: ')))
