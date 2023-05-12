import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout="wide")

data = pd.read_csv("./data/data.csv")
diagnosis = data['diagnosis'].value_counts()

#-----DEBUT---PIE--CHART-----#
# Création du pie chart avec Plotly
fig = go.Figure(
    go.Pie(
        labels=['Benign', 'Malignant'],
        values=diagnosis,
        hole=0.5,  # pour créer un donut chart, mettre cette valeur à <1
        pull=[0.1, 0, 0, 0,
              0],  # pour tirer une tranche spécifique du pie chart
        marker=dict(
            colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd'
                    ]),  # couleurs des tranches
    ))

# Réduire la taille de l'image
image = Image.open('./images/learning_curve.png')
width, height = image.size
new_size = (width * 3 // 2, height * 3 // 2)  # Diviser la taille par 2
img_resized = image.resize(new_size)

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
        <p class="text-justify">Il s'agit de la moyenne des points concaves les plus importants dans la partie la plus profonde d'une masse tumorale. Les points concaves sont des creux dans la forme de la masse tumorale. Cette caractéristique est mesurée sur une échelle numérique de 0 à 0,201.</p>

      </div>
      <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#people-circle"></use></svg>
        </div>
        <h3 class="fs-2">radius_worst</h3>
        <p class="text-justify">il s'agit de la moyenne des trois rayons les plus grands trouvés dans une masse tumorale. Cette caractéristique est mesurée en unités de longueur (millimètres).</p>

      </div>
      <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
        </div>
        <h3 class="fs-2">texture_worst</h3>
        <p class="text-justify">En général, les cellules malignes ont tendance à avoir une texture plus irrégulière et plus rugueuse que les cellules bénignes, ce qui peut conduire à une valeur plus élevée de "texture_worst" dans les échantillons de tissu mammaire malins</p>

      </div>

       <div class="feature col">
        <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
        </div>
        <h3 class="fs-2">perimeter_se</h3>
        <p class="text-justify">il s'agit de l'erreur standard du périmètre des cellules (la distance autour de la masse tumorale) trouvées dans l'image. Cette caractéristique est mesurée en unités de longueur (millimètres).</p>

      </div>

    </div>

    <img src="learning_curve.png" class="img-fluid" alt="Learning curve >

    """,
    height=600,
)

col1, col2 = st.columns((2, 2))

with col1:
    st.write("<center><h3><b>Courbe d'apprentissage</b></h3></center>",
             unsafe_allow_html=True)
    st.image(img_resized)
with col2:
    st.write("<center><h3><b>Proportion des tumeurs</b></h3></center>",
             unsafe_allow_html=True)
    st.plotly_chart(fig)
