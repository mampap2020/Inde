import streamlit as st
from src.controllers.auth import login 
from src.router import redirect
from pandas import DataFrame, read_csv
import pandas as pd
import sqlite3 as sqlite
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from src.controllers.lakeRequest import getDfLake 
from src.controllers.auth import logout
def load_view():
    st.title("Acceuil")
    
    

################
    st.markdown("""## **Bienveue sur le site**""")
   
        
    st.markdown("""Ce site permet de visualiser une analyse concernat la relation entre la production énergétique 
    et la zone géographique en inde""")
    st.markdown("""
    - Longage phython est le concepte de programme.
    - Librerie pandas pour la transformation des données.
    - Librerie matplotlib et seborne pour les graphes.
    """)
    

    














    #ax = sns.barplot(data=df.head(10), y="SUM Share", x="Region", hue="Region", dodge = False)


    #plt.title("La production de thermique par région")
    #ax.set(xlabel="Région", ylabel=None)


