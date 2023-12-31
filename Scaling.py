import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame
df = pd.read_csv(r"C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv")

# Identify numerical and categorical columns
numerical_vars = df.select_dtypes(include=['number']).columns

# Standardize numerical variables
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[numerical_vars]), columns=numerical_vars)

# Display the first few rows of the standardized DataFrame
print('First few rows of the Standardized DataFrame:')
print(df_scaled.head())

# Correlation matrix and heatmap for standardized numerical variables
correlation_matrix_scaled = df_scaled.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_scaled, annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlation Matrix (Scaled Numerical Variables)')
plt.show()
