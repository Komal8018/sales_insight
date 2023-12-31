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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming X_train and y_train are your training data
# Replace 'TargetVariable' with your actual target variable name
# Replace 'YourModel' with the name you want to give to your model
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Select a machine learning model
model = RandomForestRegressor()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the training set
train_predictions = model.predict(X_train)

# Print training performance metrics
train_rmse = mean_squared_error(y_train, train_predictions, squared=False)
print(f"Training RMSE: {train_rmse}")

# Make predictions on the test set
test_predictions = model.predict(X_test)

# Print testing performance metrics
test_rmse = mean_squared_error(y_test, test_predictions, squared=False)
print(f"Testing RMSE: {test_rmse}")
# Select a machine learning model
model = RandomForestRegressor()

# Fit the model on the training data
model.fit(X_train, y_train)
from sklearn.metrics import mean_squared_error

# Use the testing set to evaluate the model's performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
