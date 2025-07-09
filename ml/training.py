import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def train_star_classifier(data, model_path= 'classifier.pkl'):
    df = pd.read_csv(data)