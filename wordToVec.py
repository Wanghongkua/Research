#  from gensim.models import word2vec
import gensim
from provide_sentence import GetSentence
import setting


def train_word2vec():
    """train word2vec model
    :returns:

    """
    print("Training word2vec")
    sentences = GetSentence(setting.database)
    model = gensim.models.Word2Vec(
        sentences,
        window=5,
        min_count=1,
        size=80,
        workers=8,
        iter=20)

    print("Finish word2vec trainning")
    return model
