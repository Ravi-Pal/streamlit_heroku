import streamlit as st
import pandas as pd


st.write("""
# Find largest among 3 given numbers

This app find largest among 3 given numbers (value greater than the other two)
""")
#Get Input

st.header('Enter Three Numbers')

def user_input_features():
    
    number_1 = st.number_input("CNT_CHILDREN",min_value=0,max_value=20,step=1)
    number_2 = st.number_input("AMT_INCOME_TOTAL",min_value=0.0,max_value=2000000.0)
    number_3 = st.number_input("DAYS_BIRTH",min_value=-30000,max_value=0,step=1)
    

    data = {'NUMBER_1': number_1,
            'NUMBER_2': number_2,
            'NUMBER_3': number_3
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())



largest=df.max()
st.subheader('Largest Number')
st.write(largest)
