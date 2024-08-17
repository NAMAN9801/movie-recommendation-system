import streamlit as st 
import pickle
import pandas as pd 


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    results = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    movies_list = [(index, float(score)) for index, score in results]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # Fetching poster from API

        
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
movies_list = movies_list['title'].values


# Select Box
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies_list
)
st.write("You selected:", selected_movie_name)


# Button
if st.button('Recommend'):
    recommendaions = recommend(selected_movie_name)
    for i in recommendaions:
        st.write(i)