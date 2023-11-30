import numpy as np
import pickle
import streamlit as st
import string

st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('diabetes_classifier.pkl', 'rb'))

def main():
    st.sidebar.header("Diabetes Classification Tool")

    BP = st.number_input("You were high blood pressure ? (No = 0; Yes = 1)", 0,1)
    Cholesterol = st.number_input("You were high Cholesterol ? (No = 0; Yes = 1)", 0,1)
    BMI = st.number_input("What is your BMI ?", 0, 100)
    Smoke = st.number_input("Have you smoked at least 100 cigarettes in your entire life ? (No = 0; Yes = 1)", 0, 1)
    Stroke = st.number_input("Have you had a stroke ? (No = 0; Yes = 1)", 0, 1)
    HeartDis = st.number_input("Have you had coronary heart disease (CHD) or myocardial infarction (MI) ? (No = 0; Yes = 1)", 0, 1)
    PhysAct = st.number_input("Your physical activity in past 30 days - not including job ? (No = 0; Yes = 1)", 0, 1)
    Drink = st.number_input("Are you heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) ? (No = 0; Yes = 1)", 0, 1)
    GenHlth = st.number_input("Would you say that in general your health is: 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor ? ", 0, 5)
    MenHlth = st.number_input("Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during last 30 days ?", 0, 30)
    PhysHlth = st.number_input("Now thinking about your physical health, which includes physical illness and injury, for how many days during last 30 days ?", 0, 30)
    Walk = st.number_input("Do you have serious difficulty walking or climbing stairs? (No = 0; Yes = 1)", 0, 1)
    Age = st.number_input("Which group of Age you belong to ? (1 = Age 18 to 24, 2 = Age 25 to 29, 3 = Age 30 to 34, 4 = Age 35 to 39, 5 = Age 40 to 44, 6 = Age 45 to 49, 7 = Age 50 to 54, 8 = Age 55 to 59, 9 = 	Age 60 to 64, 10 = Age 65 to 69, 11 = Age 70 to 74, 12 = Age 75 to 79, 13 = Age 80 or older", 1, 13)
    Edu = st.number_input("Your education level ? (1 = Never attended school or only kindergarten, 2 = 	Grades 1 - 8 (Elementary), 3 = Grades 9 - 11 (Some high school), 4 = Grade 12 or GED (High school graduate), 5 = College 1 year to 3 years (Some college or technical school), 6 = College 4 years or more (College graduate))", 1, 6)
    Income = st.number_input("Your income range ? (1 = Less than $10,000, 2 = Less than $15,000 ($10,000 to less than $15,000), 3 = 	Less than $20,000 ($15,000 to less than $20,000), 4 = Less than $25,000 ($20,000 to less than $25,000), 5 = Less than $35,000 ($25,000 to less than $35,000), 6 = Less than $50,000 ($35,000 to less than $50,000), 7 = Less than $75,000 ($50,000 to less than $75,000), 8 = $75,000 or more", 1, 8)
    
    inputs = [[BP,Cholesterol,BMI,Smoke,Stroke,HeartDis,PhysAct,Drink,GenHlth,MenHlth,PhysHlth,Walk,Age,Edu,Income]] 

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten()
        if updated_res == 0.0:
            st.write('You are no diabetes')
        else:
            st.write('You are diabetes')

if __name__ == '__main__':
    main()



        # Age1 = st.selectbox(
    #     'Which group of Age you belong to ?',
    #     ('1 = Age 18 to 24', '2 = Age 25 to 29', '3 = Age 30 to 34', '4 = Age 35 to 39', '5 = Age 40 to 44', '6 = Age 45 to 49', '7 = Age 50 to 54', '8 = Age 55 to 59', '9 = Age 60 to 64', '10 = Age 65 to 69', '11 = Age 70 to 74', '12 = Age 75 to 79', '13 = Age 80 or older')
    # )