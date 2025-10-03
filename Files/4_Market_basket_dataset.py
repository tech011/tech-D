# Import necessary libraries 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 
 
# Step 1: Load the dataset 
# Replace 'Market_Basket.csv' with your file path 
data = pd.read_csv("basket.csv") 
 
# Step 2: Display dataset information 
print("Dataset Information:") 
print(data.info()) 
print("\nFirst 5 Rows:") 
print(data.head()) 
 
# Step 3: Preprocess data 
# Drop null values 
data.dropna(inplace=True) 
 
# Step 4: Convert categorical values into numeric format 
# Convert transaction data into one-hot encoding 
basket = pd.get_dummies(data) 
 
print("\nAfter Encoding:") 
print(basket.head()) 
 
# Step 5: Apply Apriori Algorithm 
# Generate frequent itemsets with minimum support 
frequent_itemsets = apriori(basket, min_support=0.05, 
use_colnames=True) 
 
print("\nFrequent Itemsets:") 
print(frequent_itemsets) 
 
# Step 6: Generate association rules 
rules = association_rules(frequent_itemsets, metric="lift", 
min_threshold=1.0) 
 
print("\nAssociation Rules:") 
print(rules[['antecedents', 'consequents', 'support', 'confidence', 
'lift']])
