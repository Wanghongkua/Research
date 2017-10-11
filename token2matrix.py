from stop_words import get_stop_words

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

import setting
import time

from doc2token import doc2array


def extract_matrix():
    """Using CountVectorizer to turn strings into word frequency matrix

    :returns: the matrix LDA gona use

    """
    time1 = time.time()

    #  Get the data from database
    texts, doc_names = doc2array()

    #  Need to be deleted
    #  n_features = 2000

    # Use tf (raw term count) features for LDA. Common English words, words
    # occurring in only one document or in at least 50% of the documents are
    # removed
    #  print("Extracting tf features for LDA...")
    tf_vectorizer = CountVectorizer(
        max_df=0.5,
        min_df=2,
        #  max_features=n_features,
        #  preprocessor=lambda x: x,
        analyzer='word',
        tokenizer=lda_tokenizer)
    tf = tf_vectorizer.fit(texts)

    tf = tf_vectorizer.transform(texts)
    tf_feature_names = tf_vectorizer.get_feature_names()

    #  Vocabulary set
    setting.vcb = set(tf_feature_names)

    print("Time for extract_matrix(): ", end='')
    print(time.time() - time1)

    return tf, tf_vectorizer, doc_names


def lda_tokenizer(raw):
    """self defined tokenizer

    :raw: string of content in file
    :returns: array of tokens

    """
    #  create tokenizer
    tokenizer = RegexpTokenizer(r'\w+')

    # create English stop words list
    en_stop = get_stop_words('en')

    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()

    #  make tokens
    tokens = tokenizer.tokenize(raw)

    # remove numbers
    tokens = [convert_number(i) for i in tokens]

    # remove stop words from tokens
    tokens = [i for i in tokens if i not in en_stop]

    # stem tokens
    tokens = [p_stemmer.stem(i) for i in tokens]

    return tokens


def convert_number(word):
    """convert number to special word. For example 123 to ***.

    :word: string of word
    :returns: string of word

    """
    if word.isdigit():
        word = '#'*(len(word))
    return word


if __name__ == "__main__":

    setting.init()
    tf, tf_feature_names, _ = extract_matrix()
    print("-------------------")
    print(tf)
    #  print(tf_feature_names[-1])
    #  debug
    #  print(tf.inverse_transform(texts))
