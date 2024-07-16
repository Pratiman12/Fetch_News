import pickle
import streamlit as st
fn = pickle.load(open('fn.pkl','rb'))
m = pickle.load(open('model.pkl','rb'))
t = pickle.load(open('new_train.pkl','rb'))
def predict_category(s,train=t,algo=m):
    pred=algo.predict([s])
    return train.target_names[pred[0]].split(".")[1]

st.header('_Pratiman\'s_', divider='rainbow')
st.logo("prj.png")
st.divider()
st.header('Fetch News \t:')
text=st.text_input('Enter the news : ')
if st.button('Fetch the news : '):
    st.button(f'News is from {predict_category(text)}')
    
    
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main{{
background-image: url("https://t4.ftcdn.net/jpg/06/69/71/63/240_F_669716329_vnYLDdjj7r2ErDRyIiY2OnDD7CzvuoWJ.jpg");
background-size: 100%;
background-position: top center;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
h2 {{
font-family: "Source Sans Pro", sans-serif;
text-shadow: 0 0 3px #000, 0 0 5px #0000FF;
color: rgb(250, 250, 250); 
letter-spacing: -0.005em;
padding: 1rem 0px;
margin: 0px;
line-height: 1.2;
}}
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
