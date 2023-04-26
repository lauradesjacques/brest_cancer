
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./data/data.csv")
data_cols = data.drop(['id'], axis=1)

st.title('Health Care diagnostic')
#diagnosis = st.selectbox("Features :", data_cols.columns)

#------GRAPH--------------------------

# Extraire les colonnes souhaitées
df = data.iloc[:, 0:32]

# Créer un selectbox pour la sélection de colonne
selected_column = st.selectbox("Sélectionnez une colonne", df.columns)

# Filtrer les données en fonction de la colonne sélectionnée
filtered_df = df[[selected_column, "diagnosis"]]

# Générer les graphiques
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, y=selected_column, x="diagnosis", ci=None)
ax.set_title(f"Graphique pour la colonne {selected_column}")
plt.xticks(rotation=90)
# Afficher le graphique dans Streamlit
st.pyplot(fig)



#----Fin---graph---------------

diagnosis = data['diagnosis'].value_counts()

#-----DEBUT---PIE--CHART-----#
# Création du pie chart avec Plotly
fig = go.Figure(go.Pie(
    labels=['Benign', 'Malignant'],
    values=diagnosis,
    hole=0.5, # pour créer un donut chart, mettre cette valeur à <1
    pull=[0.1, 0, 0, 0, 0], # pour tirer une tranche spécifique du pie chart
    marker=dict(colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd']), # couleurs des tranches
))
# Affichage du pie chart avec Streamlit
st.plotly_chart(fig)
#-----FIN---PIE--CHART-----#


import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>



    """,

    height=600,
)
