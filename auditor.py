import pandas as pd 

# this file audits the download csv data from yahoo finance and checks it for any errors 

# asking the user for the file they want read 

user_file = input("Please enter the name of the file you want the Tick Inspector to read: \n")

df = pd.read_csv(user_file, index_col='date', parse_dates=True)
print(df.index)
print(df.head(3))
