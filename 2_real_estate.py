import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_squared_error 
import matplotlib.pyplot as plt 
 
# 1. Create dataset 
np.random.seed(42) 
 
data = pd.DataFrame({ 
    'ID': np.arange(1, 501), 
    'flat': np.random.randint(1, 100, 500),       # Flats available 
    'houses': np.random.randint(1, 50, 500),      # Houses available 
}) 
 
# 2. Generate 'purchases' with some correlation 
data['purchases'] = ( 
    1.5 * data['flat'] + 
    2.8 * data['houses'] + 
    np.random.normal(0, 10, 500)   # Noise 
) 
 
# 3. Define independent (X) and target (y) variables 
X = data[['flat', 'houses']] 
y = data['purchases'] 
 
# 4. Split dataset into 70% training and 30% testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=0.3, random_state=1) 
 
# 5. Print training and testing sets 
print("Training Features (X_train):\n", X_train.head(), "\n") 
print("Training Target (y_train):\n", y_train.head(), "\n") 
print("Testing Features (X_test):\n", X_test.head(), "\n") 
print("Testing Target (y_test):\n", y_test.head(), "\n") 
 
# 6. Build and train linear regression model 
model = LinearRegression() 
model.fit(X_train, y_train) 
 
# 7. Print model details 
print("\nIntercept:", model.intercept_) 
print("Coefficients (flat, houses):", model.coef_) 
 
# 8. Predict on test set 
y_pred = model.predict(X_test) 
 
# 9. Evaluate model performance 
r2 = r2_score(y_test, y_pred) 
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) 
 
print(f"\nR² Score: {r2:.4f}") 
print(f"RMSE: {rmse:.4f}") 
 
# 10. Visualization: Actual vs Predicted Purchases 
plt.figure(figsize=(8,6)) 
plt.scatter(y_test, y_pred, color='blue', alpha=0.6) 
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
color='red', linewidth=2) 
plt.title("Actual vs Predicted Purchases") 
plt.xlabel("Actual Purchases") 
plt.ylabel("Predicted Purchases") 
plt.grid(True) 
plt.tight_layout() 
plt.show() 
