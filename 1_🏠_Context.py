import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Création d'un conteneur Bootstrap avec marges à 0
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
   <h1> Cancer du sein </h1>
    <p class="text-justify"> Le cancer du sein est le cancer le plus fréquent chez les
femmes dans le monde. Il représente 25 % de tous les cas
de cancer et a touché plus de 2,2 millions de personnes en
2020.</p>

<br>
<div class="text-30, font-weight-bold"> Methode de diagnostic </div>
<p class="text-justify"> Le diagnostic est une étape importante du traitement du cancer du sein qui influence lourdement le pronostic de la patiente. Pris en charge dès ses prémices, un cancer du sein offre en effet davantage de chance
de survie.
De fait, la science s’applique depuis longtemps à élaborer des méthodes de dépistage et de diagnostic
permettant de mieux identifier et catégoriser les tumeurs mammaires. </p>

<br>
<div class="text-30, font-weight-bold"> Dépistage </div>
<p class="text-justify">Le dépistage repose sur une mammographie (radiographie des seins), associée à un examen clinique des seins (observation et palpation).
En cas d’anomalie indéterminée ou suspecte, il est proposé au patient de
pratiquer une biopsie par aiguille fine (BAF) afin de prélever des cellules
dans la masse. Le prélèvement est ensuite examiné au microscope
Les caractéristiques des cellules sont ainsi étudiés, de part leur texture,
périmètre, symétrie, ect... confirmant ou non la présence de tumeur ma-
ligne ou benigne (exempt de métastase, non cancéreuse) diagnostiqué par
le professionnel de santé et/ou par l’intelligence artificielle.
</p>
<br>
<img src="https://amavea.org/wp-content/uploads/235736149_10225324693014953_787084758722787987_n.jpg" class="img-fluid" alt="benign/Malignant">

    """,
    height=840,
)
