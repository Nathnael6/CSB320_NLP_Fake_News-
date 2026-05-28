import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def clean_text(text):
    """
    Cleans and preprocesses text data.
    """

    text = text.lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    cleaned_words = [
        lemmatizer.lemmatize(word) for word in words if word not in stop_words
    ]

    return " ".join(cleaned_words)
