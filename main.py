import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    # Todo: Change picture for one of my own
    st.image("images/photo.png")

with col2:
    st.title("Bart Decoutere")
    content = """
    Hi, I am Bart. I'm currently in my first Bacherlor Engineering at the University of Ghent. In the weekends I train young sailors. In the evening I'm developing my python skills.
    """
    st.info(content)

content2 = """
        Below you can find some of the apps I have build in Python.  Feel free to contact me!
        """
st.write(content2)

df = pd.read_csv("data.csv", sep=';')

col3, empty_col, col4 = st.columns([2,0.5,2])

with col3:
    for index, row in df[::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write("[Source Code]({})".format(row['url']))
with col4:
    for index, row in df[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write("[Source Code]({})".format(row['url']))
        
