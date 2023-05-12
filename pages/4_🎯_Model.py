import streamlit as st
from predict import prediction_cancer
from services import create_table, save_formulaire
import pymysql
import streamlit.components.v1 as components
import os
st.set_page_config(layout="wide")

st.title('Page en construction')
# def create_form():
#     st.title('Patient data form')
#     # host=st.secrets.db_credentials.host
#     # user=st.secrets.db_credentials.username,
#     # passwd=st.secrets.db_credentials.password,
#     # db='breastcancer'
#     # conn = pymysql.connect(host=host,
#     #                     port=int(3306),
#     #                     user=user,
#     #                     passwd=passwd,
#     #                     db=db)

#  #   On créer la table de prédiction s'il n'existe pas.
#     #create_table(table_name="resultat", host=host, user=user, pwd=passwd, db=db)

#     # Initialisation du formulaire
#     with st.form("my_form"):
#         f1 = st.slider("Sélectionnez concave points_worst", 0.000, 0.5)
#         f2 = st.slider("Sélectionnez radius_worst ", 5.00, 40.00)
#         f3 = st.slider("Sélectionnez texture_worst", 10.00, 50.00)
#         f4 = st.slider("Sélectionnez perimeter_se ", 0.00, 10.00)
#         #submit_button = st.form_submit_button("create diagnosis")

# #     formulaire = {
# #         "f1": f1,
# #         "f2": f2,
# #         "f3": f3,
# #         "f4": f4
# #     }

# #     # Si le medecin clique sur le boutton
# #     if submit_button:

# #         # Utilisation du modèle de prédiction.
# #         # On appelle la fonction prediction_cancer() et on lui passe les réponses de l'utilisateur.
# #         pred = prediction_cancer(features=[i for i in formulaire.values()])

# #         # On inscrit la prédiction dans le dictionnaire.
# #         if pred:
# #             formulaire["predict"] = "Cancer"
# #         else:
# #             formulaire["predict"] = "No Cancer"

# #         # Enregistrement du formulaire en BDD.

# #         # On appelle la fonction save_formulaire popur enregistrer les réponses de l'utilisateur en BDD
# #         save_formulaire(conn=conn, features=[i for i in formulaire.values()])

# #         # Affichage de la prédiction
# #         if pred:
# #             components.html("""
# #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
# #     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
# #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

# #      <div class="modal-content rounded-3 shadow bg-danger">
# #       <div class="modal-body p-4 text-center">
# #         <h5 class="mb-0">Diagnosis : Brest Cancer</h5>
# #         <p class="mb-0">Malignant Tumor</p>
# #       </div>
# #     </div>
# #     """)

# #         else:
# #             components.html("""
# #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
# #     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
# #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

# #    <div class="modal-content rounded-3 shadow bg-success">
# #       <div class="modal-body p-4 text-center">
# #         <h5 class="mb-0">Diagnosis : No Cancer</h5>
# #         <p class="mb-0">Benign Tumor</p>
# #       </div>
# #     </div>
# #     """)


# create_form()
