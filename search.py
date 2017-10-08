import os

import setting
import doc_search
import process_index

from sorting_docs import sorting_docs


def search():
    """Search for query using LDA and Word2Vec
    :returns: Doc names

    """
    query = input("Type the query: ")

    #  Find the number of docs needed
    while True:
        try:
            num_doc = input("Type how many docs do you need: ")
            num_doc = int(num_doc)
            break
        except Exception:
            print("Please only type integer!")

    #  Init global variables
    setting.init()

    lda, doc_names, tf_vectorizer, reversed_index, doc_topic_index = get_index()

    que_tf = tf_vectorizer.transform(["query", query])

    #  Using reversed index to find docs
    final_docs = doc_search.regular_search(reversed_index, que_tf)

    #  Sorting docs by frequency
    #  final_docs = sorted(final_docs, key=lambda doc: doc[1], reverse=True)

    replace_num = 1
    while len(final_docs) < num_doc:
        #  TODO: needed to be done #
        final_docs = doc_search.concept_search(
            final_docs, len(final_docs), replace_num)
        replace_num += 1

    #  TODO: find out why it have 2 distribution#
    que_dis = lda.transform(que_tf)[1]

    #  Sorting final docs using LDA
    final_docs = sorting_docs(final_docs, doc_topic_index, que_dis)

    #  Print document names of final result
    print_docNames(final_docs, doc_names)
    return


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
