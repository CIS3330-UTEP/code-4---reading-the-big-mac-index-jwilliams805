#Lecture 2/12/24 Pandas Sandbox
# pip install pandas
import pandas as pd

# list_teams= ('49ers', 'Chiefs', 'Cowboys', 'Steelers')
# print (type(list_teams))

# print(list_teams)

# series_teams = pd.Series(list_teams)

# print(type(series_teams))
# print(series_teams)

# students = {'Hawaii': 'Isa', 'Ohio': 'David', 'Iowa': 'Justin', 'Colorado': 'Robert'}
# print(type(students))
# print(students)

# student_series = pd.Series(index= students.keys(), data = students.values())
# print(student_series)

# print(student_series.index)
# print(student_series.index.values)

filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)

# print(df.columns)
# print(df)
# print(df['local_price'])

# query = f"(iso_a3 == 'MEX')"
# mxn_df = df.query(query)

# print(round(mxn_df['dollar_price'].min(),2))
# print(round(mxn_df['dollar_price'].max(),2))
# print(round(mxn_df['dollar_price'].median(),2))

# query = f"(iso_a3 == 'JPN')"
# jpn_df = df.query(query)
# min_idx = jpn_df['dollar_price'].idxmin()


# print(min_idx)
# print(jpn_df.loc[min_idx])
# print(jpn_df.loc[min_idx]['dollar_price'])

# query = f"(iso_a3 == 'ARG')"
# arg_df = df.query(query)
# max_idx = arg_df['dollar_price'].idxmax()


# print(max_idx)
# print(arg_df.loc[max_idx])
# print(arg_df.loc[max_idx]['dollar_price'])

query = f"(iso_a3 == 'ARG')"
arg_df = df.query(query)

for index, row in arg_df.iterrows():
    print(index)
    print(row)