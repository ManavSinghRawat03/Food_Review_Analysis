import streamlit as st
import joblib
import pandas as pd
model=joblib.load('food_review.pkl')

st.set_page_config(page_title='Sentiment Analysis',layout='wide')
# Custom CSS
st.markdown("""
    <style>
        /* Banner styling */
        .banner {
            background: linear-gradient(to right, #ff4e50, #f9d423); /* Gradient */
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 2.5em;
            font-weight: bold;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        /* Card styling */
        .result-card {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            color: white;
        }
        .positive {
            background-color: #28a745;
        }
        .negative {
            background-color: #dc3545;
        }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown('<div class="banner">🍔🍕 Food Sentiment Prediction 👍👎</div>', unsafe_allow_html=True)

#Things on Sidebar
st.sidebar.image('Machine Learning & Food Reviews.png')
st.sidebar.header('👬About US')
st.sidebar.write('I am a ML Engineer working on Food Review Analysis')
st.sidebar.header('📞Contact Us')
st.sidebar.text('7011779258')

#Main screen
st.text('')
msg=st.text_input("💬 Enter Your Message",placeholder='Enter Your Review')

if st.button("Predict"):
    resp=model.predict([msg])
    if resp==0:
        st.title('Dislike 👎')
    else:
        st.title('Liked 👍')
        st.balloons()


st.text('Upload file for bulk prediction')
path=st.file_uploader('upload csv or txt file',type=['csv','txt'])
if path is not None:
    df=pd.read_csv(path,names=['Msg'])
    st.dataframe(df,width=700)
if st.button('Predict',key='b2'):
    df['Sentiment']=model.predict(df.Msg)
    df['Sentiment']=df['Sentiment'].map({0:"Dislike 👎",1:'Liked 👍'})
    st.dataframe(df,700)


