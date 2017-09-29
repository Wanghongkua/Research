import os
import pickle

from matrix2LDA import fit_model


#  global lda model
fitted_lda = None
index_flag = False


def build_index(database, folder_name, index_name):
    """ Fit the model and build the index

    :database: database
    :returns: index

    """
    #  TODO: Change number of topics #
    no_topics = 2

    index_path = os.path.join(folder_name, index_name)
    lda, tf, tf_vectorizer, tf_feature_names, file_names = fit_model(
        database, no_topics)

    #  find the top k document

    with open(index_path, "wb") as index_file:

        #  save lda model as index file
        pickle.dump(lda, index_file)

        #  make it global
        global fitted_lda
        fitted_lda = lda

    global index_flag
    index_flag = True

    return lda, file_names, tf_vectorizer


def fetch_index(folder_name, index_name):
    """fetch already built index
    :returns: index

    """
    global fitted_lda
    global index_flag
    if index_flag:
        #  already have the data
        lda = fitted_lda
    else:
        #  need to fetch from file
        index_path = os.path.join(folder_name, index_name)
        with open(index_path, "w") as index_file:
            lda = pickle.load(index_file)
        fitted_lda = lda
    return lda
