from transformers import pipeline

# Load pre-trained sentiment analysis model 
sentiment_analyzer = pipeline("sentiment-analysis")

# Example
review = """
I dislike you but at the end of the day you are a very good person and I admire you for that.
"""

# Analyze sentiment
result = sentiment_analyzer(review)

print(result)