import numpy as np
import pandas as pd
#import nltk
import matplotlib.pyplot as plt

data_source_url = "Tweets.csv"
airtweets = pd.read_csv(data_source_url)

plsize = plt.rcParams["figure.figsize"]
print("Data in CSV file")
print(airtweets.head())

print("Distribution of sentiments across all tweets ")
airtweets.airline_sentiment.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=["black", "orange", "green"])

airline_sentiment = airtweets.groupby(['airline', 'airline_sentiment'])
airline_sentiment = airline_sentiment.count().unstack()

airline_sentiment.plot(kind='bar', color=['black', 'blue', 'cyan'])
