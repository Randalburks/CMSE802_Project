"""
Functions to perform sentiment analysis on customer review text.
"""

from textblob import TextBlob

def get_sentiment(text):
    if text:
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    return 0.0
