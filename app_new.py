import streamlit as st
import pandas as pd


st.write("""
# Find largest among 3 given numbers

This app find largest among 3 given numbers (value greater than the other two)
""")
#Get Input

st.header('Enter Three Numbers')

def user_input_features():
    
    number_1 = st.number_input("First Number")
    number_2 = st.number_input("Second Number")
    number_3 = st.number_input("Third Number")
    

    data = {'NUMBER_1': number_1,
            'NUMBER_2': number_2,
            'NUMBER_3': number_3
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())



largest=df.max().max()
st.subheader('Largest Number-'+ str(largest))
#st.write(largest)
