import streamlit as st
from src.vues import login,home,objectif,dataset,analyse,conclusions
 
from src.router import redirect , get_route
from src.models.cookie import Cookie
from src.controllers.auth import logout
import utils as utl
st.set_page_config(page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = get_route()
    
    c = Cookie("data.json")
    valuescookie = dict(c.read())
    if valuescookie["uid"] == None and route != "/login":
        redirect("/login", reload=True)
        
    if route =="/login":  
        if valuescookie["uid"] != None:
            redirect("/home", reload=True)
        else:
            login.load_view()
        
    elif route == "/home":
        home.load_view()
    elif route == "/objectif":
        objectif.load_view()
    elif route =="/dataset":
        dataset.load_view()
    elif route =="/analyse":
        analyse.load_view()
        
    elif route == "/conclusions":
        conclusions.load_view() 
    
        
        
    elif route == "/logout":
        logout()
        redirect("/login", reload=True)
    


    else:
        redirect("/login",reload=True)
        login.load_view()
        #navigation()
navigation()
