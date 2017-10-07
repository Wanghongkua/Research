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

    _, _, tf_vectorizer, reversed_index = get_index()

    que_tf = tf_vectorizer.transform(["query", query])

    #  Using reversed index to find docs
    final_docs = regular_search(reversed_index, que_tf)
    final_docs = sorted(final_docs, key=lambda doc: doc[1], reverse=True)

    sys.exit()
    if len(final_docs) < num_doc:
        #  TODO: needed to be done #
        final_docs = concept_search(final_docs)
        pass

    #  sorting final docs using LDA
    sorting_docs()

    #  print(que_tf)
    #  print("------------------")
    #  for doc_idx, topic in enumerate(lda.transform(que_tf)):
    #  print(doc_idx, topic)


def sorting_docs(final_docs):
    """sorting final docs using LDA

    :final_docs:
    :returns: sorted final_docs

    """
    pass


def concept_search(final_docs):
    """Searching for additional docs by concept
    :returns: new final docs

    """
    pass


def regular_search(reversed_index, que_tf):
    """inverse index search

    :inverse_index:
    :que_tf:
    :returns:

    """
    terms_index = list(que_tf.nonzero()[1])
    terms_index = sorted(
        terms_index, key=lambda term: len(reversed_index[term]))
    final_docs = reversed_index[terms_index[0]]
    for i in range(1, len(terms_index)):
        final_docs = find_same_ele(final_docs, reversed_index[terms_index[i]])
        if final_docs == []:
            break
    #  print(final_docs)
    return final_docs


def find_same_ele(list1, list2):
    """find same element in 2 list

    :list1:
    :list2:
    :returns: same elements list

    """
    final_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i][0] == list2[j][0]:
            final_list.append(tuple([list1[i][0], list1[i][1]+list2[j][1]]))
            i += 1
            j += 1
        elif list1[i][0] < list2[j][0]:
            i += 1
        elif list1[i][0] > list2[j][0]:
            j += 1
    return final_list


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
