

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


def concept_search(final_docs, doc_num, replace_num):
    """Searching for additional docs by concept
    :returns: new final docs

    """

    return final_docs
