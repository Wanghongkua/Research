from scipy import stats

#  kld = stats.entropy(distributions.T[:, :, None], distributions.T[:, None, :])


def sorting_docs(final_docs, doc_topic_index, que_dis):
    """sorting final docs using LDA

    :final_docs:
    :doc_topic_index:

    :returns: sorted final_docs

    """
    doc_num = len(final_docs)
    doc_list = [None] * doc_num

    i = 0
    for index in final_docs:
        #  Build docID-entropy list
        doc_list[i] = (
            index,
            stats.entropy(
                pk=doc_topic_index[index],
                qk=que_dis))
        i += 1

    doc_list = sorted(doc_list, key=lambda doc: doc[1])

    return doc_list
