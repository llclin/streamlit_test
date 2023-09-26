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


st.title("Understanding your attachment style :grin:")
st.subheader("The application is developed to help you understand your attachment style, and provide necessary resources to help you in your relationship.")

st.image("https://clipart-library.com/images/rcnrp8jzi.jpg", caption="Understanding your attachment style", use_column_width=True)

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



with open("our_model.pkl", 'rb') as our_model:
    model = pickle.load(our_model)

if st.button('Generate my profile!'):
    with st.spinner('Wait for it...'):
        
        record = final_answer_1 + " " + final_answer_2 + " " + answer_3
        record_Series = pd.Series(record) 
        prediction = model.predict(record_Series)
        
        partner_record_Series = pd.Series(partner)
        partner_prediction = model.predict(partner_record_Series)
        

        
    st.success('Done!')
    
    if prediction == 1 and partner_prediction == 1:
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
       

      
       
    elif prediction == 0 and partner_prediction == 0:
        st.divider()
        st.write("You and your partner have the same attachment style which is ***Avoidant***.")
        st.write("Avoidant attachment style tend to be independent, self-directed, and often uncomfortable with intimacy. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=zv7ROoYCi6s&ab_channel=HeidiPriebe", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations for you :wink:")
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




    elif prediction == 0 and partner_prediction == 1:
        st.divider()
        st.write("Your attachment style is ***Avoidant*** whereas your partner's attachment style is ***Anxious***.")
        st.write(" Differences can be overcomed when we know how to communicate with different attachment styles. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=yMQ-cO-Jqmg", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations for you :wink:")
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
        



    elif prediction == 1 and partner_prediction == 0:
        st.divider()
        st.write("Your attachment style is ***Anxious*** whereas your partner's attachment style is ***Avoidant***.")
        st.write("Differences can be overcomed when we know how to communicate with different attachment styles. View the video below to understand more.")
        st.divider()

        st.video("https://www.youtube.com/watch?v=l8vcCPakbds", format="video/mp4", start_time=0)
        
        st.write("Below are some book recommendations suitable for your relationship with your partner :wink:")
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




