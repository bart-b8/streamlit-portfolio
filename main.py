import streamlit as st

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

