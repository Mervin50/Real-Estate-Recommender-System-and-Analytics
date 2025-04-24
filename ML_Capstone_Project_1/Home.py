import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
    layout="wide",  # Ensure full width for the image
)

# Change the background color to sky green using custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #87CEEB;  /* Sky Green */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Bold black heading at the top
st.markdown(
    "<h1 style='text-align: center; color: black;'>Welcome to Gurgaon Real Estate! 👋👋</h1>",
    unsafe_allow_html=True
)

# Full-width image below the heading
st.markdown(
    """
    <style>
    .banner-img {
        width: 100%;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    <img class="banner-img" src="https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/morning-in-mahattan-nyc-pawelgaul.jpg" alt="Gurgaon Skyline">
    """,
    unsafe_allow_html=True
)








