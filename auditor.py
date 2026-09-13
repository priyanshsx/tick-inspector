import pandas as pd 

# this file audits the download csv data from yahoo finance and checks it for any errors 

# asking the user for the file they want read 

user_file = input("Please enter the name of the file you want the Tick Inspector to read: ")

df = pd.read_csv(user_file, index_col='date', parse_dates=True)
# print(df.index)
# print(df.head(3))

# checking for duplicates 
duplicates = df.index.duplicated().sum()

# checking for missing dates 
calendar = pd.date_range(start=df.index.min(), end=df.index.max())
missing_dates = calendar.difference(df.index)

# checking for corrupted highs and lows where low > high 
corrupted_high_low = df[df['low'] > df['high']]

# checking for where volume is below 0 
negative_volume = df[df['volume'] < 0]

# printing data health report 
print(f"\n==========  Printing Data Health Report  ==========\n")
print(f"Duplicate rows found: {duplicates}")
print(f"Missing days found (if any): {len(missing_dates)}")
print(f"Corrupted highs and lows found (if any): {len(corrupted_high_low)}")
print(f"Negative volume (if any): {len(negative_volume)}")
print(f"\n==========  End of report  ==========\n")

if len(missing_dates) > 0:
   print(f"The missing dates are: {missing_dates}") 
if len(corrupted_high_low) > 0:
   print(f"The corrupted highs and lows are: {corrupted_high_low}")
if len(negative_volume) > 0:
   print(f"The negative volume rows are: {negative_volume}")

