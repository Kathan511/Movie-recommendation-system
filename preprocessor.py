import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import requests

with open('similarity.pkl', 'rb') as file:
 similarity=pickle.load(file)


def get_movies_name(df):
    return df['title'].values

def recommend(movie,movies):
    recommend_movies=[]
    recommend_movies_poster=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movies_list:
        recommended_movie_name=movies.iloc[i[0]]['title']
        recommend_movies.append(recommended_movie_name)
        recommend_movies_poster.append(fetch_poster(recommended_movie_name))
    return recommend_movies,recommend_movies_poster

def fetch_poster(movie_name):
    responce=requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=21655024f879ac40ea4da6141c07e6a5&query={movie_name}")

    data=responce.json()
    return "https://image.tmdb.org/t/p/w500/"+data['results'][0]['poster_path']