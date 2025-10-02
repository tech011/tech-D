import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

# 1. Create the dataset
np.random.seed(42)

# for reproducibility
data = pd.DataFrame({ 
    'ID': np.arange(1, 501),
    'TV': np.random.uniform(10, 300, 500),
    'Radio': np.random.uniform(5, 50, 500),
    'Newspaper': np.random.uniform(0, 100, 500)

})

# 2. Generate 'Sales' with some correlation
data['Sales'] = (
    0.045 * data['TV'] +
    0.187 * data['Radio'] +
    0.005 * data['Newspaper'] +
    np.random.normal(0, 1, 500)  # adding noise
)

# 3. Define independent and target variables
X = data[['TV', 'Radio', 'Newspaper']]  # capital X
y = data['Sales']

# 4. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # fixed: random_state


# 5. Print training and testing data
print("Training features (X_train): \n", X_train.head(), "\n")
print("Training target (y_train):\n", y_train.head(), "\n")
print("Testing features (X_test): \n", X_test.head(), "\n")
print("Testing target (y_test):\n", y_test.head(), "\n")

# 6. Build and train the linear regression model
model = LinearRegression()  
model.fit(X_train, y_train)

# 7. Print model coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("Feature Names:", X.columns.tolist())

# 8. Predict on test set
y_pred = model.predict(X_test)

# 9. Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 10. Visualization: Actual vs Predicted Sales
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.grid(True)
plt.tight_layout()  # fixed typo: tight layout -> tight_layout()
plt.show()

