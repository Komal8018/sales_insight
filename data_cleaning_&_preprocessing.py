import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

df= pd.read_csv(r"C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv")


numerical_columns = ['Amount', 'Profit', 'Quantity']


df.dropna(subset=numerical_columns, inplace=True)

scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

categorical_columns = ['Category', 'Sub-Category', 'PaymentMode']
label_encoder = LabelEncoder()
df[categorical_columns] = df[categorical_columns].apply(label_encoder.fit_transform)

df.drop('Order ID', axis=1, inplace=True)

print(df.head())
