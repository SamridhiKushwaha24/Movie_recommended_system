import streamlit as st
import pickle
import pandas as pd
# movie_list=pickle.load()
def recommend(movie):
    
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted((enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    print(movie_list)
    recommended_movies=[]
    for i in movie_list:
     recommended_movies.append(movies.iloc[i[0]].title)
    #  print(movies.iloc[i[0]].title)
    return recommended_movies
        
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System ")

selected_movie_name = st.selectbox(
    'how would you like to be contacted?',
    (movies['title'].values)
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
         st.write(i)