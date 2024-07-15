import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

# Twitter API credentials - Replace with your own credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to clean tweets
def clean_tweet(tweet):
    return ' '.join(re.sub(r'(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())

# Function to get sentiment analysis using TextBlob
def get_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Function to fetch tweets and perform sentiment analysis
def fetch_tweets_and_analyze(query, count=100):
    tweets = tweepy.Cursor(api.search, q=query, lang='en').items(count)
    data = pd.DataFrame(data=[clean_tweet(tweet.text) for tweet in tweets], columns=['Tweets'])
    data['Sentiment'] = data['Tweets'].apply(get_sentiment)
    return data

# Main function to analyze and visualize sentiment
def analyze_and_visualize_sentiment(query, count=100):
    # Fetch tweets and analyze sentiment
    data = fetch_tweets_and_analyze(query, count)

    # Count sentiment categories
    sentiment_counts = data['Sentiment'].value_counts()

    # Plotting
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title(f'Sentiment Analysis of Tweets related to "{query}"')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.show()

    # Print sentiment distribution
    print("\nSentiment Distribution:")
    print(sentiment_counts)

# Example usage: Analyze sentiment towards a brand/topic
if __name__
