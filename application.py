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



st.title("Understanding your attachment style :smile:")
st.subheader("The application is developed to help you understand you and your partner's attachment style, and provide necessary resources to help you in your relationship.")

st.image("https://clipart-library.com/images/rcnrp8jzi.jpg", caption="Understanding your attachment style", use_column_width=True)

st.divider()

answer_1 = st.selectbox(
    '***How would you like to be contacted?***',
    ('Email', 'Home phone', 'Mobile phone'))

answer_2 = st.radio(
    "***What's your favorite movie genre?***",
    ["Comedy", "Drama", "Documentary"])

answer_3 = st.text_area("***Please do share with us your recent experience with your partner.***")



with open("our_model.pkl", 'rb') as our_model:
    model = pickle.load(our_model)

if st.button('Generate my profile!'):
    with st.spinner('Wait for it...'):
        
        record = answer_1 + " " + answer_2 + " " + answer_3
        record_Series = pd.Series(record) 
        prediction = model.predict(record_Series)
        
    st.success('Done!')
    
    if prediction == 1:
       st.divider() 
       st.write("Your attachment style is ***Anxious***!")
       st.write("Anxious attachment types are often nervous and stressed about their relationships. They need constant reassurance and affection from their partner.")
       st.divider()
       
       
       st.video("https://www.youtube.com/watch?v=EdpaCMW1PHw&ab_channel=HeidiPriebe", format="video/mp4", start_time=0)
       
       st.write("Below are some recommendations suitable for your attachment style :wink:")
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
       
       
    else:
        st.divider()
        st.write("Your attachment style is ***Avoidant***!")
        st.write("Avoidant attachment types are extremely independent, self-directed, and often uncomfortable with intimacy. They’re commitment-phobes and experts at rationalizing their way out of any intimate situation.")
        st.divider()
        
        st.video("https://www.youtube.com/watch?v=zv7ROoYCi6s&ab_channel=HeidiPriebe", format="video/mp4", start_time=0)
        
        st.write("Below are some recommendations suitable for your attachment style :wink:")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            
            st.image('https://m.media-amazon.com/images/I/61guLW+ROHL._SY522_.jpg', width = 150, use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Healing-Avoidant-Attachment-Style-Workbook/dp/B0C9SFXJPG/ref=sr_1_1?qid=1695651557&refinements=p_27%3AHenry+Gottman&s=books&sr=1-1", use_container_width=True)

        with col2:
            
            st.image("https://m.media-amazon.com/images/I/61+YecoCnSL._SY522_.jpg", width = 150, use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Avoidant-Attachment-More-Effective-Relationships/dp/B0B2HWK7KD/ref=sr_1_3?crid=SD48F1UGEPHR&keywords=avoidant+attachment&qid=1695651614&s=books&sprefix=avoidant+attachment%2Cstripbooks%2C253&sr=1-3", use_container_width=True)

        with col3:
            
            st.image("https://m.media-amazon.com/images/I/61V-kq-2-9L._SY522_.jpg", width = 150,use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Avoidant-Attachment-Recovery-Relationships-Unhealthy/dp/B0CHLH9WWS/ref=sr_1_5?crid=SD48F1UGEPHR&keywords=avoidant+attachment&qid=1695651689&s=books&sprefix=avoidant+attachment%2Cstripbooks%2C253&sr=1-5", use_container_width=True)

       
       





