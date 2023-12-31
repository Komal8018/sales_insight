import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the DataFrame from the CSV file
df = pd.read_csv(r'C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv')

print('First few rows of the DataFrame:')
print(df.head())

# Feature Engineering
# Example: Create a new feature 'TotalSales' by combining 'Amount' and 'Profit'
df['TotalSales'] = df['Amount'] + df['Profit']

# Example: Perform one-hot encoding for categorical variables
categorical_vars = ['Category', 'Sub-Category', 'PaymentMode']

# Ensure only categorical variables are selected for encoding
df_categorical = df[categorical_vars]

# Perform one-hot encoding
encoder = OneHotEncoder(drop='first', sparse=False)
df_encoded = encoder.fit_transform(df_categorical)
df_encoded = pd.DataFrame(df_encoded, columns=encoder.get_feature_names_out(categorical_vars))

# Concatenate the encoded features with the original DataFrame
df = pd.concat([df, df_encoded], axis=1)

# Drop the original categorical columns
df.drop(categorical_vars, axis=1, inplace=True)

# Display the DataFrame with new features
print('\nDataFrame with new features:')
print(df.head())
