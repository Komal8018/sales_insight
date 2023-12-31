import pandas as pd
from sklearn.model_selection import train_test_split

print("Loading data...")
df = pd.read_csv(r'C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv')
print("Data loaded successfully.")

# Extract features (X) and target variable (y)
X = df[['Amount', 'Profit', 'Quantity', 'Category', 'Sub-Category', 'PaymentMode']]
y = df['Profit']  # Replace with your actual target variable

print("Performing one-hot encoding...")
X_encoded = pd.get_dummies(X, columns=['Category', 'Sub-Category', 'PaymentMode'], drop_first=True)
print("One-hot encoding completed.")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

print(f"Number of rows in the training set: {X_train.shape[0]}")
print(f"Number of rows in the testing set: {X_test.shape[0]}")
