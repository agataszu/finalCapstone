# finalCapstone
Capstone Project from Data Science Bootcamp

Download CSV file from Kaggle -->  https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products

# Amazon Product Reviews Sentiment Analysis

This project aims to analyze sentiment and similarity between two Amazon product reviews using SpaCy and SpaceyTextBlob for Natural Language Processing tasks.

## Overview

The provided Python script leverages SpaCy, a Natural Language Processing library, along with SpaceyTextBlob for sentiment analysis. It reads Amazon product reviews from a CSV file, preprocesses the text, performs sentiment analysis, and calculates the similarity between two selected reviews.

## Prerequisites

- Python 3.x
- Pandas
- SpaCy
- SpaceyTextBlob


## Installation

1. Clone the repository

2. Install the required dependencies:   pip install pandas spacy spacytextblob

3. Download the SpaCy English model:   python -m spacy download en_core_web_sm


## Usage

1. Place your Amazon product reviews CSV file (named `amazon_product_reviews.csv`) in the project directory.

2. Run the script:  sentiment_analysis.py

3. The script will output the selected reviews, their sentiment analysis results, and the similarity score between them.

