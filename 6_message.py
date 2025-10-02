import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

airtweets = pd.read_csv("Tweets.csv")
plt.rcParams["figure.figsize"] = (8, 6)

print("Data in CSV file")
print(airtweets.head())

print("Available columns in the CSV:")
print(airtweets.columns)

print("Distribution of sentiments across all tweets")
airtweets['sentiment'].value_counts().plot(
    kind='pie',
    autopct='%1.0f%%',
    colors=["black", "orange", "green"]
)

airline_sentiment = airtweets.groupby(['airline', 'sentiment'])['sentiment'].count().unstack()
airline_sentiment.plot(
    kind='bar',
    color=['black', 'orange', 'green']
)
plt.title("Airline-wise Sentiment Count")
plt.ylabel("Number of Tweets")
plt.show()
