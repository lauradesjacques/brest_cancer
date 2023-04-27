import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import streamlit as st
import numpy as np

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

