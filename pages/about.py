import streamlit as st


def about_page():
    st.image('apre.svg', use_column_width=True)
    st.title("About Our Project")
    st.title("A Cinematic Odyssey in Personalized Recommendation Project")

    st.write("A Cinematic Odyssey in Personalized Recommendations is a groundbreaking project that revolutionizes movie recommendations. Using a Convolutional Neural Network (CNN) and a user-friendly web interface, it provides personalized movie suggestions based on individual preferences. With features like secure login, dashboard, and real-time updates, it enhances the movie-watching experience.")

    st.header("Dataset")
    st.write(
        "We utilized The Movie Database (TMDB) dataset for our project, which includes comprehensive movie information such as titles, genres, and posters. This dataset enriched our recommendation system, allowing us to provide users with a diverse and personalized movie selection.")

    st.header("Model")
    st.write("In our project, we employed a Convolutional Neural Network (CNN) model to generate personalized movie recommendations. CNNs are a type of deep learning model commonly used for image recognition tasks. We adapted this architecture to process movie posters, extracting visual features to enhance our recommendation algorithm's accuracy and relevance.")

    st.header("APIs Used")
    st.write("We used the following APIs:")
    st.write("- TMDb API: To fetch movie information.")
    st.write("- Themoviedb.org API: To fetch movie posters.")

    st.header("Technologies Used")
    st.write("Our project is built using the following technologies:")
    st.write("- Python: For programming language.")
    st.write("- Streamlit: For building the web interface.")
    st.write("- TensorFlow: For training the CNN model.")
    st.write("- Pickle: For saving and loading the trained model.")



about_page()
