import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./data/data.csv")
data_cols = data.drop(['id'], axis=1)

st.title('Data Visualisation')
#diagnosis = st.selectbox("Features :", data_cols.columns)



# Extraire les colonnes souhaitées
df = data.iloc[:, 0:32]

# Créer un selectbox pour la sélection de colonne
selected_column = st.selectbox("Sélectionnez une colonne", df.columns)

# Filtrer les données en fonction de la colonne sélectionnée
filtered_df = df[[selected_column, "diagnosis"]]

#----START-CREATE-4-GRAPH----
# Histogram
fig1, ax = plt.subplots()
sns.histplot(data = filtered_df, x=selected_column, kde=True)
plt.show()

# Boxplot
fig2, ax = plt.subplots()
sns.boxplot(data = filtered_df, x=selected_column)
plt.show()

# Boxplot Bi-varié
fig3, ax = plt.subplots()
sns.boxplot(data = filtered_df, y=selected_column, x='diagnosis')
plt.show()

# Catplot
fig4 = sns.catplot(data=filtered_df, y=selected_column, x='diagnosis', estimator=sum)

#----END-CREATE-4-GRAPH----

# Afficher le 2 viz bloc horizontal
col1, col2 = st.columns((2,2))
with col1:
    st.pyplot(fig1)
    st.pyplot(fig3)
with col2:
    st.pyplot(fig2)
    st.pyplot(fig4)

#----Fin---graph---------------
