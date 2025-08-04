import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    "title": [
        "The Matrix",
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "The Godfather"
    ],
    "overview": [
        "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "A thief who steals corporate secrets through the use of dream-sharing technology.",
        "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "When the menace known as the Joker wreaks havoc, Batman must accept one of the greatest psychological and physical tests of his ability.",
        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["overview"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movie(title):
    if title not in df["title"].values:
        return ["Movie not found."]
    idx = df[df["title"] == title].index[0]
    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:6]
    return df["title"].iloc[[i[0] for i in sim_scores]].tolist()

# Example run
movie_name = input("Enter a movie title: ")
print(f"🎯 Recommendations for: {movie_name}")
for i, movie in enumerate(recommend_movie(movie_name), 1):
    print(f"{i}. {movie}")
