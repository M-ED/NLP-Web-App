import streamlit as st 
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
#import spacy
#import spacy_streamlit


#with st.sidebar:
 #   draw_all("sidebar")

st.title("NLP Web App")

st.write("""
                 
                 This is a Natural Language Processing Based Web App that can do anything u can imagine with the Text.
        """)
        
st.write("""
                 
                 Natural Language Processing (NLP) is a computational technique to understand the human language in the way they spoke and write.
        """)
        
st.write("""
                 
                 NLP is a sub field of Artificial Intelligence (AI) to understand the context of text just like humans.
        """)
        
        
st.image('banner_image.jpg')



   
st.subheader("Chatting")
st.write(" Enter the Context and chat with your bot based on the context!")
question_answering = pipeline("question-answering")

context = st.text_area("Context","Enter the Context Here")
        
question = st.text_area("Your Question","Enter your Question Here")
        
if context !="Enter Text Here" and question!="Enter your Question Here":
    result = question_answering(question=question, context=context)
    s1 = json.dumps(result)
    d2 = json.loads(s1)
    generated_text = d2['answer']
    generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
    st.write(f" Here's your Answer :\n {generated_text}")



## video
vid=open('chatbot_vid.mp4', 'rb').read()
st.video(vid)



  





