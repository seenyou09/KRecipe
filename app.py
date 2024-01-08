import streamlit as st 
import pandas as pd
import streamlit_pandas as sp
from PIL import Image
from src.rec_sys import rec_sys
import pandas as pd
from src import config



#Cache csv fil
@st.cache_data()
def loadKnn():
    output = pd.read_excel(config.DATABASE_URL)
    return output


image = Image.open(config.PHOTO_URL).resize((750,421))
st.image(image)

#title of the page 
st.title("Korean Culinary Ease: Simplifying Home Cooking with Your Everyday Ingredients")
import streamlit as st

import streamlit as st

st.markdown(
    "AI Model for Foodies <a href='https://github.com/seenyou09/KRecipe'><img src='https://i.ibb.co/rcwXt85/github.png' width='40' height='40' alt='GitHub'></a>",
    unsafe_allow_html=True,
)

st.markdown(
    "Credit to Maangchi for all the Korean Recipe <a href='https://www.maangchi.com/'><img src='https://i.ibb.co/zG168Bt/maangchi-pic.png' width='40' height='40' alt='maangchi'></a>",
    unsafe_allow_html=True,
)


#sidebar for options 
form1 = st.sidebar.form(key='parameter')


form1.markdown("## Let's uncover the delightful recipes waiting to be created.")


options1 = form1.text_area("Ingredients in your Fridge",
                                    'Greeen onion, pepper, kimchi')


options2 = form1.multiselect("What type of food do you want to make", [
    'side dish',
    'main dish',
    'snack',
    'appetizer',
    'dessert' 
    ])
form1.markdown("<h1 style='font-size: 10px;'>*Don't input anything if you have no preference</h1>", unsafe_allow_html=True)



options3 = form1.slider("Number of Recipes",
                                    1,50,5)

button1 = form1.form_submit_button("Submit")


#make the URL clickable
def make_clickable(name, link):

    text = name
    return f'<a target="_blank" href="{link}">{text}</a>'

if button1:
    df_recipes = loadKnn()
    trial = rec_sys(options3, options1, options2, df_recipes)
    yes = trial.get_recommendations()
    yes["EnglishName"] = yes.apply(
        lambda row: make_clickable(row["EnglishName"], row["url"]), axis=1
    )
    recipe_display = yes[["EnglishName", "KoreanName", "Ingredients"]]
    

    recipe_display_html = recipe_display.to_html(escape=False, justify='right')

    st.write(recipe_display_html, unsafe_allow_html=True)

