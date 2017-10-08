from scipy import stats

#  kld = stats.entropy(distributions.T[:, :, None], distributions.T[:, None, :])


def sorting_docs(final_docs, doc_topic_index, que_dis):
    """sorting final docs using LDA

    :final_docs:
    :doc_topic_index:

    :returns: sorted final_docs

    """
    for i in range(len(final_docs)):
        index = final_docs[i][0]

        final_docs[i] = (
            final_docs[i][0],
            stats.entropy(pk=doc_topic_index[index], qk=que_dis))

    final_docs = sorted(final_docs, key=lambda doc: doc[1])

    return final_docs
