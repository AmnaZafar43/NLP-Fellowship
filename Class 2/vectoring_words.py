from gensim.models import Word2Vec
from gensim.test.utils import datapath
from gensim import downloader as api

# Download the text8 corpus
text8_corpus = api.load("text8")

# Train a Word2Vec model
model = Word2Vec(text8_corpus, vector_size=100, window=5, min_count=5, workers=4)

# Save the model for future use
model.save("word2vec_text8.model")

# Load the model (if needed)
# model = Word2Vec.load("word2vec_text8.model")

# Example: Get the vector for a word
word = "university"
if word in model.wv:
    vector = model.wv[word]
    print(f"Vector for '{word}':\n{vector}")

# Example: Find similar words
similar_words = model.wv.most_similar(word, topn=10)
print(f"\nWords most similar to '{word}':")
for similar_word, similarity in similar_words:
    print(f"{similar_word}: {similarity:.4f}")

# Example: Perform vector arithmetic
result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print(f"\nResult of 'king' + 'woman' - 'man': {result[0][0]}")