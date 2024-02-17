import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    pass
    query_year = df[(df['iso_a3']== country_code.upper()) & (df['date'].str.startswith(year))]
    rmp_year = round(query_year ['dollar_price'].mean(),2)
    print (rmp_year)
    return rmp_year

def get_big_mac_price_by_country(country_code):
    pass
    query_country = df[df['iso_a3'] == country_code.upper()]
    rmp_country = round(query_country ['dollar_price'].mean(),2)
    print (rmp_country)
    return rmp_country

def get_the_cheapest_big_mac_price_by_year(year):
    pass
    query_cheapest = df[df['date'].str.startswith(year)]
    cheap_row = query_cheapest.loc[query_cheapest['dollar_price'].idxmin()]
    name_of_country = cheap_row['name']
    country_code = cheap_row['iso_a3']
    dollar_price = cheap_row[ 'dollar_price']
    print (f"{name_of_country}({country_code}): ${dollar_price:.2f}")
    return f"{name_of_country}({country_code}): ${dollar_price:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    pass
    query_mexpensive = df[df['date'].str.startswith(year)]
    cheap_row = query_mexpensive.loc[query_mexpensive['dollar_price'].idxmax()]
    name_of_country = cheap_row['name']
    country_code = cheap_row['iso_a3']
    dollar_price = cheap_row[ 'dollar_price']
    print (f"{name_of_country}({country_code}): ${dollar_price:.2f}")
    return f"{name_of_country}({country_code}): ${dollar_price:.2f}"

if __name__ == "__main__":
    # pass
    get_big_mac_price_by_year(str(input("Enter year: ")), input('Enter country code: '))
    get_big_mac_price_by_country((input("Enter country code: ")))
    get_the_cheapest_big_mac_price_by_year(str(input('Enter year: ')))
    get_the_most_expensive_big_mac_price_by_year(str(input('Enter year: ')))
    