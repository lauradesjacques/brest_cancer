import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import streamlit as st
import numpy as np
import streamlit.components.v1 as components
import plotly.graph_objs as go


def create_table(table_name:str):
    #engine=create_engine('mysql+pymysql://root:@localhost/cancer')
    engine = create_engine("mysql+pymysql://root:Root1234+@localhost:3306/cancer")
    inspector=inspect(engine)
    if not table_name in inspector.get_table_names():

        # Initialisation des colonnes.
        df = pd.DataFrame({'f1':[] , 'f2':[], "f3":[], "f4":[], "predict":[]})

        # Typage des colonnes de la Table SQL.
        df['f1'    ]  = df['f1'    ].astype('float64')
        df['f2' ]  = df['f2' ].astype('float64')
        df['f3' ]  = df['f3' ].astype('float64')
        df['f4' ]  = df['f4' ].astype('float64')
        df['predict']  = df['predict'].astype('str')

        # envoie du DataFrame sur SQL.
        df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)

### Fonction permettent d'enregistrer le formulaire en BDD (la target et les features).
### Les paramètres : la connexion à la BDD, et une liste des features.
def save_formulaire(conn, features:list):
    cursor = conn.cursor()
    sql = "INSERT INTO resultat (f1, f2, f3, f4, predict) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, features)
    conn.commit()
    conn.close()
