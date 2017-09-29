import os

#  import sys
#  from sklearn.feature_extraction.text import CountVectorizer

import process_index

#  from token2matrix import lda_tokenizer

query = input("Type the query: ")

#  TODO: this need to be changed #
folder_name = "index_folder"
index_name = "index_file"
database = "simple"

if not os.path.isdir(folder_name):
    os.makedirs(folder_name)
    lda, _, tf_vectorizer = process_index.build_index(
        database, folder_name, index_name)
else:
    lda = process_index.fetch_index(folder_name, index_name)

que_tf = tf_vectorizer.transform(["query", query])
print(que_tf)
print("------------------")
for doc_idx, topic in enumerate(lda.transform(que_tf)):
    print(doc_idx, topic)
