import pandas as pd 
df= pd.read_csv(r"C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv")
# data exploring
print(df.head())
print(df.describe())
#looking for missing data
missing_values = df[df.isnull().any(axis=1)]
print("\nRows with Missing Values:")
print(missing_values)
#Handling the missing data 
df = df.bfill(inplace=True)