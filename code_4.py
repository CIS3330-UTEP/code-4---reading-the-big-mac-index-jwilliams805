import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    pass
    query_year = df[(df['iso_a3']== country_code.upper()) & (df['date'].startswith(year))]
    rmp_year = round(query_year ['dollar_price'].mean(),2)
def get_big_mac_price_by_country(country_code):
    pass
    query_country = df[df['iso_a3'] == country_code.upper()]
    rmp_country = round(query_country ['dollar_price'].mean(),2)
    print (rmp_country)
    return rmp_country

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    # pass
    get_big_mac_price_by_country((input("Enter country code: ")))
    # get_big_mac_price_by_year(int(input('Enter year: ')),str(input("Enter country code: ")))