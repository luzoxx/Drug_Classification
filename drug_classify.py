import numpy as np
import pickle
import streamlit as st
import string

st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('drug_classifier.pkl', 'rb'))

def main():
    st.sidebar.header("Drug Classification Tool")

    Age = st.slider("Input your Age:", 15,75)
    Sex = st.slider("Input your Gender 0 for Female and 1 for Male", 0,1)
    BP = st.slider("Input your Blood pressure 0 for High 1 for Low and 2 for Normal", 0, 2)
    Cholesterol = st.slider("Input your Cholesterol 0 for High 1 for Normal", 0, 1)
    Na_to_K = st.slider("Input your Na_to_K", 0.0, 39.0)
    inputs = [[Age, Sex, BP, Cholesterol, Na_to_K]]

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(int)
        if updated_res == 0:
            st.write('Drug Y')
        elif updated_res == 1:
            st.write('Drug A')
        elif updated_res == 2:
            st.write('Drug B')
        elif updated_res == 3:
            st.write('Drug C')
        else:
            st.write('Drug X')

if __name__ == '__main__':
    main()
