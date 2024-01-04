import streamlit as st 
import pandas as pd


# streamlit run page.py 
st.title("Korean food recommmedation")
  
#use checkbox
st.header("This is a checkbox header")
like = st.checkbox("DO you like this app?")
        

#button number 2 
st.header("This is the radio header")
#radio feature
animal =  st.radio("What is you favorite food", ('Main dish', 'side dish','dessert'))
button2 = st.button("submit")
if button2:
    if button2:
        st.write(animal)
    else:
        st.write("please do the checkbox")
        
    
st.header("This is the selectbox header")        
#selectbox
favfood = st.selectbox("What is you favorite food", ('Main dish', 'side dish','dessert'))
button3 = st.button("submit2")
if button3:
    if button3:
        st.write(favfood)
    else:
        st.write("please do the checkbox")


st.header("Start of the Multiselect Section")
options = st.multiselect("What food do you like",["kimchi","rice","stew"])
button4 = st.button("Select")
if button4:
    if button4:
        st.write(options)
        


st.header("this is the slider section")
epoch_num = st.slider('how many epoch',1,100,10)


st.header("this is the text input section")
user_text =st.text_input("What is your favorite food", 'kimchi')
                         
st.header("this is the text area section")
txt = st.text_area("casdcascdascasd")


#How to cache models in streamlit 
@st.cache_data()
def loadKnn():
    output = pd.read_excel('/Users/seanyoo/Desktop/korean_food_project/xlsx/koreanFood_data.xlsx')
    return output
model = loadKnn()



#session state
counter = 0
if "counter" not in st.session_state:
    st.session_state.counter = 0


if st.button("up"):
    st.session_state.counter +=1 
    st.write(st.session_state.counter)

if st.button("reset"):
    st.session_state.counter = 0
    st.write(st.session_state.counter)
    
    
    
#Using containers 
main_container = st.container()

main_container.button("this is the main container button")
