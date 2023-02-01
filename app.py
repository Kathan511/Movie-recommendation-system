import streamlit as st
import preprocessor
import pandas as pd

df=pd.read_csv("final_df.csv")

st.title("Movie Recommender System")

col_names=preprocessor.get_movies_name(df)

selected_movie_name=st.selectbox("Select the movie name:",col_names)

if st.button("🍿Recommend Movies🍿"):
    st.header("Your Recommended Movies are:")
    names,posters=preprocessor.recommend(selected_movie_name,df)
    
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])