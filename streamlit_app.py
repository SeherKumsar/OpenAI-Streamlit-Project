import streamlit as st
from langchain.llms import OpenAI
# pip install streamlit openai langchain
# pip install -U langchain-community
# streamlit run streamlit_app.py

st.title("My-First-AI-App") # Title of the app

openai_api_key = st.sidebar.text_input("OpenAI API Key") # Text input in the sidebar

def response(input_text):
    llm = OpenAI(temperature=0.7, # Higher temperature means the model will take more risks(more chaotic text)
                 openai_api_key = openai_api_key,) # OpenAI API Key
    st.info(llm(input_text)) # Display the output

# widget
with st.form("my_form"):
    text = st.text_area("Enter Text: ", # Text area in the main body
                        "Write three tips for learning NLP.") # Default text
    submitted = st.form_submit_button("Submit") # Submit button
    if not openai_api_key.startswith("sk-"): # Check if the API key is valid (key starts with "sk")
        st.warning("Please enter your OpenAI API Key!", icon="⚠️") # Display warning
    if submitted and openai_api_key.startswith("sk-"): # If the submit button is clicked and the API key is valid
        response(text) # Call the response function

st.markdown("Made with ❤️ by [Seher Kumsar](https://github.com/SeherKumsar)") # Display text in markdown format