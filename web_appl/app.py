# ----------------------------
# Core Packages
# ----------------------------
import streamlit as st
st.set_page_config(
    page_title="NLP Web App",
    page_icon="👍",
    layout="centered",
    initial_sidebar_state="auto"
)

# ----------------------------
# NLP Packages
# ----------------------------
from textblob import TextBlob
import spacy
import neattext as nt

# ----------------------------
# Visualization Packages
# ----------------------------
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


# ----------------------------
# Main App Function
# ----------------------------
def main():
    """NLP Web App with Streamlit"""

    # --- Title Section ---
    title_html = """
    <div style="background-color:blue; padding:10px; border-radius:5px;">
        <h1 style="color:white; text-align:center;">NLP Web App</h1>
    </div>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    # --- Subheader Section ---
    subheader_html = """
    <div style="background-color:lightblue; padding:6px; border-radius:5px;">
        <h3 style="color:black; text-align:center;">Powered by Streamlit 🚀</h3>
    </div>
    """
    st.markdown(subheader_html, unsafe_allow_html=True)

    # --- Sidebar Menu ---
    menu_options = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Select Activity", menu_options)

    # --- Page Logic ---
    if choice == "Text Analysis":
        st.subheader("📘 Text Analysis")
        st.write("Enter your text in the input field to analyze it.")

    elif choice == "Translation":
        st.subheader("🌐 Translation")
        st.write("Translate text between different languages.")

    elif choice == "Sentiment Analysis":
        st.subheader("💬 Sentiment Analysis")
        st.write("Check the sentiment (positive, negative, neutral) of your text.")

    elif choice == "About":
        st.subheader("ℹ️ About")
        st.markdown("""
        ### NLP Web App made with [Streamlit](https://streamlit.io)  
        This app demonstrates basic Natural Language Processing features:
        - Text Cleaning
        - Translation
        - Sentiment Analysis
        - Word Clouds (coming soon)
        """)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    main()
