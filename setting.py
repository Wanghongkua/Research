def init():
    """Init globle variables
    :returns: None

    """
    global database
    database = "simple"

    global folder_name
    folder_name = "index_folder"

    global vcb

    #  Index File Names {{{
    global word2vec_file
    word2vec_file = "word2vec_file"

    global vcb_file
    vcb_file = "vcb_file"

    global vcb_set
    vcb_set = "vcb_set"

    global lda_model
    lda_model = "lda_model"

    global doc_topic_index
    doc_topic_index = "doc_topic_index"

    global doc_names
    doc_names = "doc_names"

    global reversed_file
    reversed_file = "reversed_file"

    #  }}}

    global no_topics
    #  TODO: Change number of topics #
    no_topics = 2
