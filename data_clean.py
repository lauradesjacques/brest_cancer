import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

data_clean = pd.read_csv("./data/result.csv")
data = data_clean.drop(['Unnamed: 0'], axis=1)
