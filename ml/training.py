import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def train_star_classifier(data= '/hr_spec/ml/data/refined_data/6_class.csv', model_path= 'classifier.pkl'):
     
    df = pd.read_csv(data)

    # necessary columns
    cols = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
            'Absolute magnitude(Mv)', 'Star type', 'Star color', 
            'Spectral Class']
    
    if not all(col in df.columns for col in cols):
        raise ValueError(f'Column {cols} not found from dataframe')
    

    # define label and input features
    X = df[['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
            'Absolute magnitude(Mv)', 'Star type', 'Star color']]
    y = df['Spectral Class']
