import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import streamlit as st
import numpy as np
import streamlit.components.v1 as components

def create_table(table_name:str):
    engine=create_engine('mysql+pymysql://root:@localhost/cancer')
    inspector=inspect(engine)
    if not table_name in inspector.get_table_names():

        # Initialisation des colonnes.
        df = pd.DataFrame({'id':[], 'f1':[] , 'f2':[], "f3":[], "diagnosis":[]})

        # Typage des colonnes de la Table SQL.
        df['id'   ]  = df['id'   ].astype('id')
        df['f1'    ]  = df['f1'    ].astype('float64')
        df['f2' ]  = df['f2' ].astype('float64')
        df['diagnosis']  = df['diagnosis'].astype('str')

        # envoie du DataFrame sur SQL.
        df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)
    print(f"Création de la table {table_name} avec succès.")




# Fonction qui vérifie si l'entrée est un nombre à virgule
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Affiche une alerte si l'entrée n'est pas un nombre à virgule
def show_alert():
    st.components.v1.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div class="alert alert-danger" role="alert">
            Veuillez entrer un nombre à virgule valide.
        </div>
        """,
        height=50
    )

def show_valid():
    st.components.v1.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div class="alert alert-success" role="alert">
            Ce champ est bien valide.
        </div>
        """,
        height=50
    )
