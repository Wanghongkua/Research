import setting


def build_inverse(tf):
    """Build inverse index for each word

    :tf: the CountVectorizer fitted model
    :returns:
        indexex: 2d array of term, doc frequency

    """
    i = 0
    vcb_size = len(setting.vcb)
    print("vcb_size:", vcb_size)
    indexes = [None] * vcb_size
    while True:
        try:
            doc = tf[i].toarray()

            #  TODO: save memory #
            for term_id in range(vcb_size):
                if doc[0][term_id] != 0:
                    if indexes[term_id] is None:
                        indexes[term_id] = []
                    indexes[term_id].append(tuple([i, doc[0][term_id]]))

            i += 1
        except IndexError:
            break
    return indexes
