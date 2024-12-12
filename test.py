import streamlit as st

st.set_page_config(
    page_title="Recommendation App",
    page_icon="👋",
)
st.image('home.svg', use_column_width=True)
st.title('Movie Recommendation')
st.write("""
    This project aims to build a recommendation system for movies using collaborative filtering.
    Collaborative filtering is a technique used by recommender systems to make automatic predictions about the interests of a user by collecting preferences from many users.

    ### Dataset
    The dataset used for this project is the MovieLens dataset, which contains movie ratings by users.
    
    ### Methodology
    - Data Preprocessing: Cleaned the dataset and performed exploratory data analysis (EDA).
    - Collaborative Filtering: Implemented collaborative filtering using the cosine similarity method.
    
    ### Results
    The recommendation system successfully provides movie recommendations based on user preferences.
    
    ### Future Work
    - Improve recommendation accuracy by incorporating more advanced algorithms.
    - Enhance the user interface for a better user experience.
    
    
    """)
st.image('homepage.svg', use_column_width=True)

st.sidebar.success("select a page above")
