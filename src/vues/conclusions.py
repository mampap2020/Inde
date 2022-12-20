import streamlit as st

from src.router import redirect 

def load_view():

    st.markdown("conclusions")
    
    if st.button("conclusions"): 
        redirect("/login", reload=True)