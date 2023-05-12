import streamlit as st
import numpy as np
from data_clean import data
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification
import pickle

### Fonction pour faire la prédiction.
### Les paramètres : On donne en paramètre les features.
def prediction_cancer(features:list):

    # Modèle
    model = pickle.load(open("./data/pipeline_vf.pkl","rb"))

    x = np.array([i for i in features]).reshape(1, 4)
    X_df = pd.DataFrame(x, columns=["concave points_worst","radius_worst","texture_worst","perimeter_se"])

    # Prédictions résultat
    predict = model.predict(X_df)
    if predict == 0:
        return False
    return True
