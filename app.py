import pickle
import streamlit as st
import webbrowser
import string

global lang_model

lang = open('model.pkl','rb')
lang_model=pickle.load(lang)
lang.close()
# Giving title to webpage:
st.title("Language Detection Tool :")
# Adding text box for inputing text form the user:
input_test = st.text_input("Provide your text here 👇","My name is jhon cena")
# now making a submit button:
button_submit = st.button("Get language name")
# making above button work:
if button_submit:
    st.text(lang_model.predict([input_test]))