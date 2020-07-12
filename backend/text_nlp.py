import nltk
from nltk import word_tokenize
from nltk import corpus
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.util import ngrams


#wnl = WordNetLemmatizer()

def get_stop_words():
    stopword_list = corpus.stopwords.words('german')
    return stopword_list

def tokenize_text(text):
    list_words = word_tokenize(text, language="german")
    list_words = [word.strip() for word in list_words]
    bigram = list(ngrams(list_words, 2))
    trigrams = list(ngrams(list_words,3))
    return list_words, bigram, trigrams


def get_vectors_together(list):
    full_text=""
    for i in list:
        full_text+=i
    return full_text


#full_text=get_vectors_together(extracted_information)

def feature_extractor(train_data):
    vectorizer = CountVectorizer()
    X_train=vectorizer.fit_transform(train_data)
    return vectorizer, X_train


