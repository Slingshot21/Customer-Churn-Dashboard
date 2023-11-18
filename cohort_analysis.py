import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from datetime import date, datetime

@st.experimental_memo
st.set_page_config(
    page_title = "Cohorts Dashboard",
    page_icon = "",
    layout = "wide"
)

@st.experimental_memo
def purchase_rate(customer_id):
    purchase_rate = [1]
    counter = 1
    for i in range(l,len(customer_id)):
        if customer_id[i] != customer_id[i-1]:
            purchase_rate.append(1)
            counter = 1
        else:
            counter += 1
            purchase_rate.append(counter)
    return purchase_rate

@st.experiemental_memo
def join_date(date, purchase_date):
    join_date = list(range(len(date)))
    for i in range(len(purchase_date)):
        if purchase_rate[i] == 1:
            join_date[i] = date[i]
        else:
            join_date[i] = date[i-1]
    return join_date


st.title("Cohort Interactive Dashboard")
st.markdown("""
Performs Cohort Analysis of your_company data!

* **Libraries taken from python are : ** base64,pandas, numpy, streamlit, matplotlib, seaborn
* **Data Source** : **[Store](link)
* PLease upload data to analyze the results
""")
uploaded_file = st.file_uploader = ("choose a file") #to upload the necessary file\

if uploaded_file is not None:    #this is important because without this,
                                #when there is no file uploaded, there will an error that df is not defined. 
    df = pd.read_csv(uploaded_file)
    df_processed = process_df(df)

#dashboard_title
st.header("Live Dashboard")
#Filters
first_filter = st.selectbox('select first filter', ['Option 1','Option 2', 'Option3'])
second_filter = st.selectbox('Select second filter', ['Option 1', 'Option 2', 'Option 3'])

output = display_function(data_input, first_filter, second_filter)
st.dataframe(output)
st.download_button(label = 'Download Csv', data = output.to_csv(), mime = 'text/csv') #to download the file


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_processed = process_df(df)
    df_cohorts = cohort_numbers(df_processed)
    cohorts = cohort_percent(df_cohorts)

    #dynamic title by using f-strings
    st.header(f"Live {cohorts.index[0]} to {cohorts.index[-1]} Cohort Dashboard")

    #Filters
    first_filter = st.selectbox('Select type of cohort', ['By Unique Customers', 'By Percentage(%)', 'By Average Order Value(AOV)'])
    second_filter = st.selectbox('Select cohort', list(cohorts.index))

    output = select_which_table_to_draw(df_processed, first_filter, second_filter)
    st.dataframe(output)
    st.download_button(label = 'Download Csv', data = output.to_csv(), mime = 'text/csv') #to download the file

