import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_squared_error 
import matplotlib.pyplot as plt 
import numpy as np 
 
# 1. Load dataset 
# Replace 'Fish.csv' with your local path or the raw URL 
data = pd.read_csv('Fish.csv') 
 
# 2. Select feature and target 
X = data[['Length3']]  # Independent variable 
y = data['Weight']     # Target variable 
 
# 3. Split into training (70%) and testing (30%) sets 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.3, random_state=42) 
 
# 4. Print sample data 
print("Training feature sample:\n", X_train.head(), "\n") 
print("Training target sample:\n", y_train.head(), "\n") 
print("Testing feature sample:\n", X_test.head(), "\n") 
print("Testing target sample:\n", y_test.head(), "\n") 
 
# 5. Build and train a simple linear regression model 
model = LinearRegression() 
model.fit(X_train, y_train) 
 
# 6. Model output 
print("Intercept:", model.intercept_) 
print("Coefficient for Length3:", model.coef_[0]) 
 
# 7. Make predictions on test set 
y_pred = model.predict(X_test) 
 
# 8. Evaluate model performance 
r2 = r2_score(y_test, y_pred) 
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) 
print(f"R² Score: {r2:.4f}") 
print(f"RMSE: {rmse:.4f}") 
 
# 9. Visualize actual vs predicted weight 
plt.figure(figsize=(8, 6)) 
plt.scatter(X_test, y_test, color='blue', alpha=0.6, label='Actual weight') 
plt.plot(X_test, y_pred, color='red', linewidth=2, 
label='Prediction') 
plt.title("Fish Weight Prediction: Actual vs Predicted (Length3)") 
plt.xlabel("Length3") 
plt.ylabel("Weight") 
plt.legend() 
plt.grid(True) 
plt.tight_layout() 
plt.show() 
