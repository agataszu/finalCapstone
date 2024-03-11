import pandas as pd
import spacy
# Importing SpaceyTextBlob for sentiment analysis
from spacytextblob import spacytextblob 

# Loading spaCy model
nlp = spacy.load('en_core_web_sm')

# Adding SpaceyTextBlob to the spaCy pipeline
nlp.add_pipe('spacytextblob')

# Loading dataset
data = pd.read_csv('amazon_product_reviews.csv')

# Selecting the 'reviews.text' column
reviews_data = data['reviews.text']

# Removing missing values and updating 'data' DataFrame
data = data.dropna(subset=['reviews.text'])

# Preprocessing text data
def preprocess_text(text):
    # Converting text to lowercase
    text = text.lower()
    # Removing leading and trailing whitespaces
    text = text.strip()
    # Tokenizing the text
    doc = nlp(text)
    # Removing stopwords and punctuation, and lemmatizing the tokens
    processed_text = ' '.join(token.lemma_ for token in doc if not token.is_stop and not token.is_punct)
    return processed_text

# Creating function for sentiment analysis
def analyze_sentiment(text):
    doc = nlp(text)
    # Extracting polarity using SpaceyTextBlob
    polarity = doc._.polarity
    return polarity


# Mapping polarity scores to sentiment labels
def map_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Selecting two random product reviews from the 'reviews.text' column
review1 = data['reviews.text'].iloc[37]  
review2 = data['reviews.text'].iloc[2148] 

# Printing selected reviews to be able to judge the code calculation output vs what we (humans) interpret as similar review
print("Review 1:")
print(review1)
print("\nReview 2:")
print(review2)

# Preprocessing the selected reviews
processed_review1 = preprocess_text(review1)
processed_review2 = preprocess_text(review2)


# Calculating sentiment for the selected reviews
sentiment_review1 = analyze_sentiment(processed_review1)
sentiment_review2 = analyze_sentiment(processed_review2)

# Mapping polarity scores to sentiment labels
sentiment_label_review1 = map_sentiment(sentiment_review1)
sentiment_label_review2 = map_sentiment(sentiment_review2)

# Calculating similarity between the two reviews
doc1 = nlp(processed_review1)
doc2 = nlp(processed_review2)
similarity_score = doc1.similarity(doc2)

# Printing the similarity score
print(f"\nSimilarity score between review 1 and review 2: {similarity_score}")

# Checking if reviews are similar and their sentiment
if sentiment_label_review1 == sentiment_label_review2:
    print("\nThe reviews have similar sentiment, implying a", sentiment_label_review1, "sentiment.")
    if similarity_score > 0:
        print("Additionally, the reviews are similar.")
else:
    print("\nThe reviews have different sentiment.")
