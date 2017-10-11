#  from gensim.models import word2vec
import gensim
from provide_sentence import GetSentence
import setting
import time


def train_word2vec():
    """train word2vec model
    :returns:

    """
    #  print("Training word2vec")

    time1 = time.time()

    sentences = GetSentence(setting.database)
    print("Time for GetSentence(): ", time.time() - time1)
    model = gensim.models.Word2Vec(
        sentences,
        window=2,
        min_count=1,
        size=80,
        workers=4,
        iter=20)

    print("Time for train_word2vec(): ", end='')
    print(time.time() - time1)

    #  print("Finish word2vec trainning")
    return model
