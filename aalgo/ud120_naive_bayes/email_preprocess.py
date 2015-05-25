#!/usr/bin/python
"""Parse the ENRON email data for the naive Bayes project."""

import pickle
import numpy

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from fractions import Fraction


def preprocess(words_file="../tools/word_data.pkl", authors_file="../tools/email_authors.pkl"):
    """
    Take a pre-made list of email texts (by default word_data.pkl) and the corresponding authors (by default email_authors.pkl) and preprocesses them.

    Preprocessor steps:
        - split into training/testing sets (10% testing)
        - vectorize into tfidf matrix
        - select/keep most helpful features

    After this, the feaures and labels are put into numpy arrays, which play nice with sklearn functions

    A tfidf matrix is defined as TF(t)*IDF(t) where
    TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
    IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

    4 objects are returned:
        -- training/testing features
        -- training/testing labels
    """
    # the words (features) and authors (labels), already largely preprocessed this preprocessing will be repeated in the text learning mini-project
    print('words_file = {}'.format(words_file))
    word_data = pickle.load(open(words_file, "rb"))
    authors = pickle.load(open(authors_file, "rb"))

    # test_size is the percentage of events assigned to the test set (remainder go into training)
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

    # text vectorization--go from strings to lists of numbers
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    # feature selection, because text is super high dimensional and can be really computationally chewy as a result
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    # info on the data
    print("no. of Chris training emails:", sum(labels_train))
    print("no. of Sara training emails:", len(labels_train) - sum(labels_train))

    #for value in features_train_transformed[0]:
        #frac = Fraction(float(value))
        #if frac > 0:
            #print(frac)

    return numpy.array(features_train_transformed), numpy.array(features_test_transformed), numpy.array(labels_train), numpy.array(labels_test)
