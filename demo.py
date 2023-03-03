#1.import libraries
import pandas as pd
import streamlit as st
import numpy as np

#2.set up the page configuration for my analysis
st.set_page_config(
    page_title="Live Cohort Analysis"
    page_icon = #check the docs and add it 
    layout= "wide"
    
)

#3.define all functions used in my project. 
#4. for every function, add "@st.experimental_memo" in front of it. THis is to memorize each function execution. This would make the app run faster, 
#when the users interact with some elements on the  dashboard

@st.experimental_memo
def function(x):
    return y


