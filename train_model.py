import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load your dataset (replace 'your_dataset.csv' with your actual dataset file)
dataset = pd.read_csv('data.csv')

# Assume 'price' is the target variable, and other columns are features
features_cols = ["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront",
                  "view", "condition", "sqft_above", "sqft_basement", "yr_built", "yr_renovated"]

X = dataset[features_cols]
y = dataset["price"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the trained model to a file named 'model.pkl'
joblib.dump(model, 'model.pkl')
