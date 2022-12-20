import streamlit as st 
from src.controllers.auth import login
from src.router import redirect
def load_view():
    st.title("Page de connexion")
    mail = st.text_input(" Email")
    password = st.text_input('mot de passe', type='password')
   

    if st.button("se connecter"):
        if login(mail, password):
            
            redirect("/home", reload=True)

        else:
            st.text("Erreur de connexion")
        
    
            