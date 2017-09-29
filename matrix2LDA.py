from sklearn.decomposition import LatentDirichletAllocation
#  from sklearn.feature_extraction.text import CountVectorizer

from token2matrix import extract_matrix


def fit_model(database, no_topics=2):
    """Fit LDA with database

    :database:
    :returns:

    """
    #  Pre-processing
    tf, tf_vectorizer, tf_feature_names, file_names = extract_matrix(database)

    #  Fit the modle
    lda = LatentDirichletAllocation(
        n_topics=no_topics,
        max_iter=5,
        learning_method='online',
        learning_offset=50.,
        random_state=0).fit(tf)

    print("Finish LDA training")
    #  no_top_words = 10
    #  display_docs(lda, tf_feature_names, no_top_words, tf)
    return lda, tf, tf_vectorizer, tf_feature_names, file_names


def display_docs(model, file_names, no_top_words, tf):
    """
    For debug
    Deisplay the doc topics distrubution

    """
    for doc_idx, topic in enumerate(model.transform(tf)):
        print(doc_idx, file_names[doc_idx])
        print(" ".join(["topic"+str(i)
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

    print()


def display_topic(model, feature_names, no_top_words):
    """
    For debug
    Deisplay the topic words distrubution

    """
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


if __name__ == "__main__":
    #  for debug

    #  database = "NSWSC_txt"
    database = "simple"
    flag = 0
    if flag == 1:
        no_top_words = 10
        lda, tf, tf_feature_names, _ = fit_model(database, no_topics=2)
        display_topic(lda, tf_feature_names, no_top_words)
    else:
        no_top_topics = 3
        lda, tf, _, file_names = fit_model(database, no_topics=2)
        display_docs(lda, file_names, no_top_topics, tf)
