import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def create_similarity_matrix():
    movies = pd.read_csv("movie-recommendation/movies.csv")
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies["title"])
    similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    return movies, similarity_matrix

def get_movie_recommendations(movies, similarity_matrix, movie_title):
    index = movies[movies["title"] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_10_similar_movies = similarity_scores[1:11]
    movie_indices = [i[0] for i in top_10_similar_movies]
    return movies["title"].iloc[movie_indices]

if __name__ == "__main__":
    movie_title = "Sabrina (1995)"
    movies, similarity_matrix = create_similarity_matrix()
    recommendations = get_movie_recommendations(movies, similarity_matrix, movie_title)
    print(f"{movie_title} için film tavsiyeleri:")
    print(recommendations)

