import os

import setting

import sys
import process_index

#  from token2matrix import lda_tokenizer


def search():
    """Search for query using LDA and Word2Vec
    :returns: Doc names

    """
    query = input("Type the query: ")

    #  Init global variables
    setting.init()

    lda, _, tf_vectorizer, reversed_index = get_index()

    que_tf = tf_vectorizer.transform(["query", query])

    regular_search(reversed_index, que_tf)
    sys.exit()

    print(que_tf)
    print("------------------")
    for doc_idx, topic in enumerate(lda.transform(que_tf)):
        print(doc_idx, topic)


def regular_search(reversed_index, que_tf):
    """inverse index search

    :inverse_index:
    :que_tf:
    :returns:

    """
    print(que_tf)
    pass


def get_index():
    """get index
    :returns: TODO

    """
    if not os.path.isdir(setting.folder_name):
        print("Building index")
        os.makedirs(setting.folder_name)
        return process_index.build_index()
    else:
        print("Fetching index")
        return process_index.fetch_index()

    #  if not os.path.isdir(setting.folder_name):
    #  print("Building index")
    #  os.makedirs(setting.folder_name)
    #  lda, _, tf_vectorizer, reversed_index = process_index.build_index()
    #  else:
    #  print("Fetching index")
    #  lda, _, tf_vectorizer, reversed_index = process_index.fetch_index()


if __name__ == "__main__":
    search()
