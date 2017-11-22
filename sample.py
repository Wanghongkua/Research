
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.layers import Input, Dense
from keras.models import Sequential
from keras import optimizers

def read_text_data(path):
    filenames = glob.glob(path + "/*.txt")
    filenames.sort()
    result_list = []
    for filename in filenames:
        content = open(filename, "r").read()
        result_list.append(content)
    return result_list, filenames

n_features = 400

data_samples, filenames = read_text_data("/home/wesley/Desktop/temporary/LDA/sample_text")

# Bag of Word model
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(data_samples)
tfidf = tfidf.toarray()

"""
tfidf = [
	[1, 0, 0, 0, 1, 1, 1, 0, ..., 0],		-> doc 1
	[0, 0, 0, 1, 1, 2, 0, 1, ..., 2],		-> doc 2
	...
]
"""

# Keras

middle_dim   = 10
encoding_dim = 2

# Layers
layer_before = Dense(middle_dim, input_dim=n_features, activation="sigmoid" )			# W1
encode_layer = Dense(encoding_dim, input_dim=middle_dim, activation="softmax")		# W2
decode_layer = Dense(middle_dim, input_dim=encoding_dim, activation="tanh")			# W3
layer_after  = Dense(n_features, input_dim=middle_dim, activation="tanh" )			# W4

optimizer   = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

autoencoder = Sequential()
autoencoder.add(layer_before)
autoencoder.add(encode_layer)
autoencoder.add(decode_layer)
autoencoder.add(layer_after)
autoencoder.compile(optimizer=optimizer, loss='binary_crossentropy')
autoencoder.fit(tfidf, tfidf, epochs=4000, batch_size=10, shuffle=True)


encoder = Sequential()
encoder.add(layer_before)
encoder.add(encode_layer)
encoder.compile(optimizer=optimizer, loss='binary_crossentropy')
output = encoder.predict(tfidf)

print(output)
