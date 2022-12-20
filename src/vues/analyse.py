import streamlit as st
from src.controllers.lakeRequest import getDfLake 
from src.router import redirect 
import seaborn as sns
import numpy as np
import streamlit as st
from src.controllers.auth import login 
from src.router import redirect
from pandas import DataFrame, read_csv
import pandas as pd
import sqlite3 as sqlite
import matplotlib.pyplot as plt
from src.controllers.lakeRequest import getDfLake 
from src.controllers.auth import logout
import plotly.express as px





def load_view():

    
    
    
    
    #df = read_csv("src/assets/State_Region_corrected.csv")
    #st.dataframe(df) 
    
    
    #st.dataframe(getDfLake("select Region from State_Region_corrected "))
    
    df=getDfLake("""
    SELECT 
         
        "Area (km2)",
        "National Share (%)",
        "State / Union territory (UT)"
    FROM 
        State_Region_corrected 
    
    """) 
    

    st.dataframe(df)
    st.markdown("""La part d'électricité de chaque états:""")
    fig = plt.figure()

    sns.barplot(df.sort_values('National Share (%)',ascending=False),x='Area (km2)',y='State / Union territory (UT)')
        
    plt.title('La part délectricité de chaque états')
    st.pyplot(fig)
    #####################################
    
    df[["National Share (%)", "Area (km2)"]].corr()
    
    
    fig = px.scatter(df, x="Area (km2)", y="National Share (%)")
    
    st.plotly_chart(fig)
    
########################################################


##La part d'électricité de chaque région :
    
    st.markdown("""La part d'électricité de chaque région :""")


    df=getDfLake("""
    SELECT 
        Region, 
        SUM("National Share (%)") AS 'SUM Share'
    FROM 
        State_Region_corrected 
    group by 
        Region
    """) 
    st.dataframe(df)


    fig = plt.figure()
    region = df["Region"].unique()
    nb_region = len(region)
    plt.pie(df['SUM Share'],labels=df["Region"],autopct='%1.0f%%',explode=[0.05]*nb_region)
    plt.title(label="La part d'électricité de chaque région",fontsize=10,fontstyle='oblique')
    st.pyplot(fig)

    

    st.markdown("""Le graphe montre que la zone la plus consommatrice de l'énergie électrique c'est le Nord de l'inde avec 28% , 
    après c'est  le sud avec 20% et la zone la moins consommatrice de l'électricité en Inde c'est nord-est  avec 8% """)
     ########################################
    ###
    st.markdown("""La part de la production des énergies de chaque région :""")
    df = read_csv("src/assets/file_02.csv")
    st.dataframe(df)
    df=getDfLake("""
    SELECT 
        Region, 
        SUM("Thermal Generation Actual (in MU)") AS 'Sum_Thermal',
        SUM("Nuclear Generation Actual (in MU)") AS 'Sum_Nuclear',
        SUM("Hydro Generation Actual (in MU)") AS 'Sum_Hydro'
    FROM 
        file_02
    group by 
        Region
    """) 
    st.dataframe(df)

    # Pie Chart 
    fig = plt.figure()
    region = df["Region"].unique()
    nb_region = len(region)
    plt.pie(df['Sum_Thermal'],labels=df["Region"],autopct='%1.0f%%',explode=[0.05]*nb_region)
    plt.title(label="La production termique par region",fontsize=10,fontstyle='oblique')
    plt.show()
    st.pyplot(fig)
############################
    fig = plt.figure()
    ax = sns.barplot(data=df.head(10), y="Sum_Thermal", x="Region", hue="Region", dodge = False)
    ax.set(xlabel="Région", ylabel=None)

    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[0].set_text("Eastern")
    i.get_texts()[1].set_text("NorthEastern")
    i.get_texts()[2].set_text('Northern')
    i.get_texts()[3].set_text("Southern")
    i.get_texts()[4].set_text("Western")
    st.pyplot(fig)
    st.markdown(""" les graphe montre que la production de thermique est concentrer plus dans le West de l'inde , 
    40% de l'énergie thermique est produit  dans West de l'inde , 22% et 20% produit dans nord et le sud de l'inde respectivement, 16% dans le Est, 
    mais le Nord-est est zone la moins productive de l'énergie thermique elle représente juste 1% de la production thermique en inde.""")

    
    fig = plt.figure()
    ax = sns.barplot(data=df.head(10), y="Sum_Nuclear", x="Region", hue="Region", dodge = False)

    plt.title("La production de nucleare par région")
    ax.set(xlabel="Région", ylabel=None)

    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[0].set_text("Eastern")
    i.get_texts()[1].set_text("NorthEastern")
    i.get_texts()[2].set_text('Northern')
    i.get_texts()[3].set_text("Southern")
    i.get_texts()[4].set_text("Western")
    st.pyplot(fig)
    st.markdown("""Selon le graphe on voit que la production de nucléaire est concentrer plus dans le  Sud  de l'inde, 
    plus de la moitié de nucléaire est produit dans le sud, 
    et l'autre moitié est produit dans le Nord et West de l'inde""")
     #####################################
    fig = plt.figure()
    region = df["Region"].unique()
    nb_region = len(region)
    plt.pie(df['Sum_Thermal'],labels=df["Region"],autopct='%1.0f%%',explode=[0.05]*nb_region)
    plt.title(label="La production hydrolique par region",fontsize=10,fontstyle='oblique')
    plt.show()
    st.pyplot(fig)
    #####################
    fig = plt.figure()
    ax = sns.barplot(data=df.head(10), y="Sum_Hydro", x="Region", hue="Region", dodge = False)

    plt.title("La production de l'hydraulique par région")
    ax.set(xlabel="Région", ylabel=None)

    
    st.pyplot(fig)


    
    st.markdown("""les graphes montrent  que la production de l'hydraulique  est concentrer plus dans le  nord de l'inde,
    plus de la moitié(52%) de l'hydraulique est produit dans le nord , 20% est produit dans le sud """)
    
    
    
    
    
    
    #####################################################   
    st.markdown("""L'evolution des énergies dans le temps :""") 
    df1=getDfLake("""
    SELECT
        Region,
        strftime("%Y",Date) As year,
        SUM("Thermal Generation Actual (in MU)") AS 'Sum_Thermal',
        SUM("Nuclear Generation Actual (in MU)") AS 'Sum_Nuclear',
        SUM("Hydro Generation Actual (in MU)") AS 'Sum_Hydro'
        
            
    FROM 
        file_02
    group by 
            Region,
            year


        
    """)
    st.dataframe(df1)
    st.markdown("""L'evolution de l'énergie thermique :""") 
    fig = plt.figure()
    sns.lineplot(data=df1, x="year", y="Sum_Thermal", hue="Region")
    
    st.pyplot(fig)
    ##########
    fig = plt.figure()
    st.markdown("""L'evolution de l'énergie nucléaire :""") 
    sns.lineplot(data=df1, x="year", y="Sum_Nuclear", hue="Region")
    st.pyplot(fig)
    ###########
    st.markdown("""L'evolution de l'énergie hydraulique:""")
    fig = plt.figure()
    
    sns.lineplot(data=df1, x="year", y="Sum_Hydro", hue="Region")
    st.pyplot(fig)
