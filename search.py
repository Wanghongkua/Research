import os
import sys

import setting
#  import doc_search
import process_index

from sorting_docs import sorting_docs
from doc_search import find_docs


def search():
    """Search for query using LDA and Word2Vec
    :returns: Doc names

    """

    #  Get user query request
    query, num_doc = get_input()

    #  Init global variables
    setting.init()

    #  Get index needed to do search
    lda, doc_names, tf_vectorizer, reversed_index,\
        doc_topic_index, wordToVec = get_index()

    #  Pre-process query terms
    que_tf = tf_vectorizer.transform([query])

    #  Find Matched Documents ID
    final_docs = find_docs(
        reversed_index,
        que_tf,
        num_doc,
        tf_vectorizer,
        wordToVec)

    #  Ranking docs
    que_dis = lda.transform(que_tf)[0]

    #  Sorting final docs using LDA
    final_docs = sorting_docs(final_docs, doc_topic_index, que_dis)

    #  Print document names of final result
    print_docNames(final_docs, doc_names)

    return


def get_input():
    """get query and number of docs needed
    :returns: TODO

    """
    query = sys.argv[1]
    #  query = input("Type the query: ")

    #  Find the number of docs needed
    while True:
        try:
            #  num_doc = input("Type how many docs do you need: ")
            num_doc = sys.argv[2]
            num_doc = int(num_doc)
            break
        except Exception:
            print("Please only type integer!")

    return query, num_doc


def print_docNames(final_docs, doc_names):
    """print document names of search result

    :final_docs:
    :doc_names:
    :returns: None

    """
    for i in range(len(final_docs)):
        index = final_docs[i][0]
        print(doc_names[index])


def get_index():
    """get index
    :returns:

    """
    if not os.path.isdir(setting.folder_name):
        print("Building index")
        os.makedirs(setting.folder_name)
        return process_index.build_index()
    else:
        print("Fetching index")
        return process_index.fetch_index()


if __name__ == "__main__":
    search()
