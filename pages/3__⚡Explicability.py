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
   <h1> Explicabilité </h1>
    <p class="text-justify"> Solution d'aide au diagnostic, grâce à un modèle
d’apprentissage supervisé, nous allons classifier des cas de tumeurs malignes ou bénignes grâce aux différentes caractéristiques des noyaux cellulaires.
Notre modèle répondra aux besoins des spécialistes de l’image médicale afin d’affirmer ou non la précense d’une tumeur cancéreuse.</p>

<div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
      <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#collection"></use></svg>
        </div>
        <h3 class="fs-2">concave points_worst</h3>
        <p>l s'agit de la moyenne des points concaves les plus importants dans la partie la plus profonde d'une masse tumorale. Les points concaves sont des creux dans la forme de la masse tumorale. Cette caractéristique est mesurée sur une échelle numérique de 0 à 0,201.</p>

      </div>
      <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#people-circle"></use></svg>
        </div>
        <h3 class="fs-2">radius_worst</h3>
        <p>il s'agit de la moyenne des trois rayons les plus grands trouvés dans une masse tumorale. Cette caractéristique est mesurée en unités de longueur (millimètres).</p>

      </div>
      <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
        </div>
        <h3 class="fs-2">texture_worst</h3>
        <p>il s'agit de la moyenne de la déviation standard des valeurs de la couleur gris de l'image de la masse tumorale. Cette caractéristique est mesurée sur une échelle numérique de 0 à 43,88.</p>

      </div>

       <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
        </div>
        <h3 class="fs-2">perimeter_se</h3>
        <p>il s'agit de l'erreur standard du périmètre des cellules (la distance autour de la masse tumorale) trouvées dans l'image. Cette caractéristique est mesurée en unités de longueur (millimètres).</p>

      </div>

    </div>



    """,
    height=2000,
)
