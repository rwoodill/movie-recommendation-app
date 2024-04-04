import streamlit as st
import pickle
import requests
from api import api_key

def fetch_poster(id):
    base_url = "https://api.themoviedb.org/3/movie/{}?language=en-US&api_key="
    url = base_url + api_key
    full_url = url.format(id)
    data = requests.get(full_url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")

select_value = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommendations = []
    poster_list = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommendations.append(movies.iloc[i[0]].title)
        poster_list.append(fetch_poster(movie_id))

    return recommendations, poster_list

if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])   
        st.image(movie_poster[1]) 
    with col3:
        st.text(movie_name[2]) 
        st.image(movie_poster[2])   
    with col4:
        st.text(movie_name[3]) 
        st.image(movie_poster[3])   
    with col5:
        st.text(movie_name[4]) 
        st.image(movie_poster[4])   


