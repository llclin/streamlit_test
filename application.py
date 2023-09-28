#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:23:06 2023

@author: licheng
"""



import streamlit as st
import numpy as np
import time
from PIL import Image
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer



st.title("Understanding you and your partner's attachment style :blush:")
st.subheader("The application is developed to help you understand you and your partner's attachment style, and provide necessary resources to help you in your relationship.")

st.image("https://clipart-library.com/images/rcnrp8jzi.jpg", caption="Understanding you and your partner's attachment style", use_column_width=True)

st.divider()


answer_1 = st.selectbox(
    '***How will you react if your partner leaves you?***',
    ('That is his or her loss', 'I will be sad, devastated'))
if answer_1 =='That is his or her loss':
    final_answer_1 = "avoidant"
else:
    final_answer_1 = "anxious"

answer_2 = st.radio(
    "***How often do you talk to your partner about your feelings?***",
    ["Seldom", "Quite Often"])

if answer_2 =='Seldom':
    final_answer_2 = "avoidant"
else:
    final_answer_2 = "anxious"

answer_3 = st.text_area("***Please share how you felt about an argument you had with your partner.***")


partner = st.selectbox(
    '***How does your partner typically react in an argument?***',
    ('My partner will give me a cold shoulder', 'My partner will become very emotional'))
if partner == "My partner will give me a cold shoulder":
    final_partner ="avoidant"
else:
    final_partner="anxious"



with open("our_model.pkl", 'rb') as our_model:
    model = pickle.load(our_model)

with open('our_vectorizer.pkl', 'rb') as vect:
    vectorizer = pickle.load(vect)
    


if st.button('Generate profile!'):
    with st.spinner('Wait for it...'):
        
        user = final_answer_1 + " " + final_answer_2 + " " + answer_3
        user_series = pd.Series(user)
        user_record = vectorizer.transform(user_series)
        prediction = model.predict(user_record)
        
        
        partner_series = pd.Series(final_partner)
        partner_record = vectorizer.transform(partner_series)
        partner_prediction = model.predict(partner_record)
        

        
    st.success('Done!')
    
    if prediction ==1  and partner_prediction ==1 :
       st.divider() 
       st.write("You and your partner have the same attachment style which is ***Anxious***.")
       st.write("Anxious attachment style tend to be nervous and stressed about their relationships. View the video below to understand more.")
       st.divider()

       st.video("https://www.youtube.com/watch?v=EdpaCMW1PHw&ab_channel=HeidiPriebe", format="video/mp4", start_time=0)
       
       st.write("Below are some recommendations for you :wink:")
       col1, col2, col3 = st.columns(3, gap="medium")
       with col1:
           
           st.image("https://img1.od-cdn.com/ImageType-100/1523-1/%7BF2891E67-123A-4785-AFD2-862D4DE36200%7DImg100.jpg", width = 150, use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/6889424", use_container_width=True)

       with col2:
           
           st.image("https://img1.od-cdn.com/ImageType-100/1219-1/%7B502BBD28-C4A1-4C12-BEC6-CD66C797430E%7DImg100.jpg", width = 150, use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/5901249", use_container_width=True)

       with col3:
           
           st.image("https://img1.od-cdn.com/ImageType-100/1523-1/%7B73A45BAA-C1B6-4DE1-A907-97F1DEBCE31E%7DImg100.jpg", width = 150,use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/5168313", use_container_width=True)
           

       st.write(" ")
       with st.chat_message("user"):
           st.write("Hello👋 We hope that the above resources have been helpful.")
           st.write("If you need more support and would like to chat with someone:") 
           st.link_button("Click for more assistance", "https://familyassist.msf.gov.sg/content/resources/programmes/online-counselling/")
       

      
       
    elif prediction == 0 and partner_prediction == 0:
        st.divider()
        st.write("You and your partner have the same attachment style which is ***Avoidant***.")
        st.write("Avoidant attachment style tend to be independent, self-directed, and often uncomfortable with intimacy. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=zv7ROoYCi6s&ab_channel=HeidiPriebe", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations for you :wink:")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            
            st.image('https://img1.od-cdn.com/ImageType-100/1430-1/%7BC70BEA75-D280-43F2-AEFF-1E5EEB5CD8F6%7DImg100.jpg', width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/319596", use_container_width=True)

        with col2:
            
            st.image("https://img1.od-cdn.com/ImageType-100/0044-1/%7BED3699EC-C269-4B4E-AA44-9BC0970FB606%7DImg100.jpg", width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/3682131", use_container_width=True)

        with col3:
            
            st.image("https://img1.od-cdn.com/ImageType-100/1430-1/%7BEC8D5943-429E-4F9C-B446-5D6600E3AB57%7DImg100.jpg", width = 150,use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/322424", use_container_width=True)

        
        st.write(" ")
        with st.chat_message("user"):
            st.write("Hello👋 We hope that the above resources have been helpful.")
            st.write("If you need more support and would like to chat with someone:") 
            st.link_button("Click for more assistance", "https://familyassist.msf.gov.sg/content/resources/programmes/online-counselling/")


    elif prediction == 0 and partner_prediction == 1:
        st.divider()
        st.write("Your attachment style is ***Avoidant*** whereas your partner's attachment style is ***Anxious***.")
        st.write(" Differences can be overcomed when we know how to communicate with different attachment styles. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=yMQ-cO-Jqmg", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations for you :wink:")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            
            st.image("https://img1.od-cdn.com/ImageType-100/12293-1/%7B054D9E58-B7ED-45E4-9C97-CCEE8BFD6433%7DIMG100.JPG", width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/5054551", use_container_width=True)

        with col2:
            
            st.image("https://img1.od-cdn.com/ImageType-100/1219-1/%7B502BBD28-C4A1-4C12-BEC6-CD66C797430E%7DImg100.jpg", width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/5901249", use_container_width=True)

        with col3:
            
            st.image("https://img1.od-cdn.com/ImageType-100/1523-1/%7B73A45BAA-C1B6-4DE1-A907-97F1DEBCE31E%7DImg100.jpg", width = 150,use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/5168313", use_container_width=True)
        
        st.write(" ")
        with st.chat_message("user"):
            st.write("Hello👋 We hope that the above resources have been helpful.")
            st.write("If you need more support and would like to chat with someone:") 
            st.link_button("Click for more assistance", "https://familyassist.msf.gov.sg/content/resources/programmes/online-counselling/")


    else: #prediction == 1 and partner_prediction == 0:
        st.divider()
        st.write("Your attachment style is ***Anxious*** whereas your partner's attachment style is ***Avoidant***.")
        st.write("Differences can be overcomed when we know how to communicate with different attachment styles. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=l8vcCPakbds", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations for you :wink:")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            
            st.image('https://img1.od-cdn.com/ImageType-100/1523-1/%7BD7320176-CE10-4830-9F86-2142B5F595B3%7DImg100.jpg', width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/204069", use_container_width=True)

        with col2:
    
            st.image('https://img1.od-cdn.com/ImageType-100/1430-1/%7BC70BEA75-D280-43F2-AEFF-1E5EEB5CD8F6%7DImg100.jpg', width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/319596", use_container_width=True)

        with col3:
    
            st.image("https://img1.od-cdn.com/ImageType-100/0044-1/%7BED3699EC-C269-4B4E-AA44-9BC0970FB606%7DImg100.jpg", width = 150, use_column_width="always")
            st.link_button("Click to read more","https://nlb.overdrive.com/media/3682131", use_container_width=True)

        st.write(" ")
        with st.chat_message("user"):
            st.write("Hello👋 We hope that the above resources have been helpful.")
            st.write("If you need more support and would like to chat with someone:") 
            st.link_button("Click for more assistance", "https://familyassist.msf.gov.sg/content/resources/programmes/online-counselling/")

