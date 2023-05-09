import streamlit as st
from predict import prediction_cancer
from services import create_table, save_formulaire
import pymysql

st.set_page_config(layout="wide")

def create_form():
    st.title('Patient data form')

    # Connexion à la BDD.
    conn=pymysql.connect(host='localhost',port=int(3306),user='root', passwd='Root1234+', db='cancer')

    # On créer la table de prédiction s'il n'existe pas.
    create_table(table_name="resultat")

    # Initialisation du formulaire
    min_value = 0.00
    max_value = 100.00

    with st.form("my_form"):
        #name = st.text_input("Nom du patient", max_chars=50)
        f1 = st.slider("Sélectionnez concave points_worst", 0.000, 0.5)
        f2 = st.slider("Sélectionnez radius_worst ", 5.00, 40.00)
        f3 = st.slider("Sélectionnez texture_worst", 10.00, 50.00)
        f4 = st.slider("Sélectionnez perimeter_se ", 0.00, 10.00)
        submit_button = st.form_submit_button("create diagnosis")

    formulaire = {
        #"name": name,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f4": f4
    }

# Si le medecin clique sur le boutton
    if submit_button:

    # Utilisation du modèle de prédiction.
    # On appelle la fonction prediction_cancer() et on lui passe les réponses de l'utilisateur.
        pred = prediction_cancer(features=[i for i in formulaire.values()])

    # On inscrit la prédiction dans le dictionnaire.
        if pred:
            formulaire["predict"] = "Cancer"
        else:
            formulaire["predict"] = "No Cancer"

        # Enregistrement du formulaire en BDD.
        # On appelle la fonction save_formulaire popur enregistrer les réponses de l'utilisateur en BDD
        save_formulaire(conn=conn, features=[i for i in formulaire.values()])

        # Affichage de la prédictions.
        if pred:
            st.header("Cancer !")
        else:
            st.header("Pas de cancer")


create_form()
