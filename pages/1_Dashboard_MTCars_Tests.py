import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image
import seaborn as sns
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "hornet.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "mtcars.csv")

st.title("Motor Trend Car Road Tests")
st.subheader("mtcars data is taken from 1974 motor trend US magzine , contains info about fuel consumption and 11 different aspects of 32 cars model, mpg=miles per gallon , cyl=number of cylinders , disp=displacement in inch^3, hp=horse power, drat=rear axel tation , wt = wt in pounds ....etc ")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

#models = st.selectbox("Select the model:", df['model'].unique())
st.subheader("Click Below to see values")
btn_mpg = st.button("mpg")
if btn_mpg == True:
    st.subheader("mpg")
    st.bar_chart(df, y = 'mpg', x='model')
btn_cyl = st.button("cyl")
if btn_cyl == True:   
    st.subheader("cyl")
    st.bar_chart(df, y = 'cyl', x='model')
btn_disp = st.button("disp")
if btn_disp ==True:
    st.subheader("disp")
    st.bar_chart(df, y = 'disp', x='model')
btn_hp = st.button("hp")
if btn_hp == True:  
    st.subheader("Horse Power")
    st.bar_chart(df, y='disp', x='model')
btn_drat = st.button("drat")
if btn_drat == True:
    st.subheader("drat")
    st.bar_chart(df, y='drat', x='model')
btn_wt = st.button("wt")    
if btn_wt == True:
    st.subheader("wt")
    st.bar_chart(df, y='wt', x='model')
btn_qsec = st.button("qsec")
if btn_qsec == True:
    st.subheader("qsec")
    st.bar_chart(df, y='qsec', x='model')        