from datetime import datetime
import pickle
import backend.text_nlp as tnlp
from PDFMining.settings import *
from backend.sources import *
import pandas as pd
import backend.html_to_structured_text as html_to_structured_text
import backend.pdf_to_html as pdf_to_html
import backend.information_extraction as ie
import re
# from backend.preparation.corpus_use import get_vec, vec_similarity, get_category_vecs, word2vec_model
import numpy
import pandas as pd
# Donart

"""
Retrieve the model
"""
# filename = 'backend/machine_learning/version6.0_svm_c_model.sav'
# filename2 = 'backend/machine_learning/version1.0_mlp_c_model.sav'
# filename3 = 'backend/machine_learning/version1.0_cv_model_headline.sav'
# filename_headline_mlp = 'backend/machine_learning/version1.0_mlp_c_model_headline.sav'
# filename_headline_svm = 'backend/machine_learning/version1.0_svm_c_model_headline.sav'

svm_clf = pickle.load(open(sources['svm_c'], 'rb'))
mlp_clf = pickle.load(open(sources["mlp_c"], 'rb'))
# cv = pickle.load(open(sources['count_vectorizer'], 'rb'))
mlp_clf_headline = pickle.load(open(sources['headline_mlp_c'], 'rb'))
svm_clf_headline = pickle.load(open(sources['headline_svm_c'], 'rb'))
# word2vec = word2vec_model

#category vectors fetched from category descriptions
# category_vecs = get_category_vecs(word2vec)
# DONART
def predictResult(vlerat):
    lista2 = [vlerat]
  
    df2 = pd.DataFrame(lista2)

    clf = svm_clf.predict(df2)

    return clf[0]  #ose clf 



def information_to_dataset(information_extracted):
    dataset = pd.read_csv(sources['dataset'], encoding='unicode_escape')  #utf_8_sig
    keywords = dataset.columns[3:]


    tokens, bigrams, trigrams = tnlp.tokenize_text(information_extracted)

    dict_of_frequencies = {}
    for keyword in keywords:
        dict_of_frequencies[keyword] = 0

    for keyword in keywords:
        for token in tokens:
            if token.casefold() == keyword.casefold():
                dict_of_frequencies[keyword] += 1
        for bigram in bigrams:
            new_bigram = bigram[0] + " " + bigram[1]

            if new_bigram.casefold() == keyword.casefold():
                dict_of_frequencies[keyword] += 1

                if bigram[0].casefold() in keywords:
                    if bigram[0].casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram[0].casefold()] -= 1

                if bigram[1].casefold() in keywords:
                    if bigram[1].casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram[1].casefold()] -= 1

        for trigram in trigrams:
            new_trigram = trigram[0] + " " + trigram[1] + " " + trigram[2]
            bigram1 = trigram[0] + " " + trigram[1]
            bigram2 = trigram[1] + " " + trigram[2]

            if new_trigram.casefold() == keyword.casefold():
                dict_of_frequencies[keyword] += 1

                if bigram1.casefold() in keywords:
                    if bigram1.casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram1.casefold()] -= 1

                if bigram2.casefold() in keywords:
                    if bigram2.casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram2.casefold()] -= 1

                if bigram1.casefold() in keywords and bigram2.casefold() in keywords:
                    if trigram[0].casefold() in keywords:
                        if trigram[0].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[0].casefold()] += 1

                    if trigram[1].casefold() in keywords:
                        if trigram[1].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[1].casefold()] += 1

                    if trigram[2].casefold() in keywords:
                        if trigram[2].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[2].casefold()] += 1

    return list(dict_of_frequencies.values())

info = None
