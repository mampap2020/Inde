import streamlit as st

from src.router import redirect 
from pandas import DataFrame, read_csv

def load_view():

    st.markdown("dataset/jeu de données")
    
    

    st.markdown("""## **Présentation des dataset**""")
    
    df = read_csv("src/assets/file_02.csv")
    st.dataframe(df)
    st.markdown("""  file_02, permet de visualiser la production des différentes énergies part date et par région.

    Dataset2:

    Contexte du dataset :  

    Le dataset, file_02, représente 4 périodes allant de 2016 à 2020, il a 4949 lignes  et 11 colonnes. 

    Liste des colonnes du dataset : 

    Data of generation : date de production de (01/09/2017), jusqu’a (01/08/2020) 

    Generation région : les régions de production  (Nord, Sud, Est, Ouest, Centre). 

    Actual thermal power generation: la production thermique réelle . 

    Tentative thermal power generation: la production thermique provisoire. 

    Actual nuclear  power generation: la production nucléaire réelle. 

    Tentative nuclear power generation: la production nucléaire provisoire.  

    Actual hydro power generation: la production hydroélectrique réelle.  

    Tentative hydro power generation: la production hydroélectrique provisoire. 
 """)
    df = read_csv("src/assets/region_cordinates.csv")
    st.dataframe(df)
    df = read_csv("src/assets/State_Region_corrected.csv")
    st.dataframe(df)
    st.markdown("""Dataset State_Region_corrected, ma permet de visualiser chaque état de l’inde, sa surface en mètre carré, et sa position géographique , et sa part  de production électrique  dans la production national.  

    Contexte du dataset : 

    Le dataset contient 34 lignes et 5 colonnes  

    Liste des colonnes de dataset : 

    State / Union territ(string) : les états de l’inde . 

    Area (float) : le kilométrage de chaque états . 

    Région(string): la géographie de chaque états . 

    National Share(int): la part de chaque états dans la distribution nationale d'électricité. 

    """)