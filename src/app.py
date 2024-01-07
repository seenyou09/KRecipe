
import streamlit as st 
import pandas as pd
import streamlit_pandas as sp
import altair as altcd 

from rec_sys import rec_sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import unidecode, ast

#Cache csv fil
@st.cache_data()
def loadKnn():
    output = pd.read_excel('/Users/seanyoo/Desktop/KRecipe/xlsx/kreciepe.xlsx')
    return output


#title of the page 
st.title("Korean food recommmedation")

#sidebar for options 
form1 = st.sidebar.form(key='parameter')
form1.header("What is in your pantry")
options1 = form1.text_area("", "Greeen onion, pepper, kimchi")

form1.header("What Type of food do you want to make")
options2 = form1.multiselect('',[
    'side dish',
    'main dish',
    'snack',
    'appetizer',
    'dessert' 
    ])


form1.header("Number of recipes")
options3 = form1.slider('',1,20,5)

button1 = form1.form_submit_button("submit")

if button1:
    df_recipes = loadKnn()
    trial = rec_sys(options3, options1, options2, df_recipes)
    yes = trial.get_recommendations()
    st.write(yes)
