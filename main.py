import streamlit as st
from database import create_database
from services import is_float, show_alert, show_valid

def main():
    st.title('Patient database app')
    create_database()

# Creation des Zones de saisie pour les entrées de l'utilisateur
# Vérifie si l'entrée est un nombre à virgule et affiche une alerte si nécessaire



    name = st.text_input("Nom du patient",max_chars=50)

    # area_se = st.number_input("Area_se du patient")
    # if area_se != "" and not is_float(area_se):
    #     show_alert()
    # if is_float(area_se) == True:
    #     show_valid()

    #texture_mean = st.text_input("Texture_mean du patient")

    min_value = 0.00
    max_value = 600.00
    # Sliders pour l'utilisateur et affiche les valeurs sélectionnées
    slider_area_se = st.slider("Sélectionnez Area_se", min_value, max_value)
    st.write("Vous avez sélectionné : ", slider_area_se)

    slider_texture_mean = st.slider("Sélectionnez texture_mean", min_value, max_value)
    st.write("Vous avez sélectionné : ", slider_texture_mean)

    slider_smoothness_mean = st.slider("Sélectionnez smoothness_mean", min_value, max_value)
    st.write("Vous avez sélectionné : ", slider_smoothness_mean)



    # smoothness_mean = st.text_input("Smoothness_mean du patient")

    # texture_se = st.number_input("Texture_se du patient")
    # smoothness_se = st.number_input("Smoothness_se du patient")
    # texture_worst = st.number_input("Texture_worst du patient")
    # smoothness_worst = st.number_input("Smoothness_worst du patient")


if __name__ == "__main__":
    main()
