import pandas as pd
from sklearn.model_selection import train_test_split
from classifier import KNNClassifier
import joblib

def train_star_classifier(data= 'ml/data/refined_data/6_class.csv', k= 3): 
        
        '''
        load dataset 
        '''
        
        df = pd.read_csv(data)

        # columns from data set
        cols = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
                'Absolute magnitude(Mv)', 'Star type', 'Star color', 
                'Spectral Class']
        
        if not all(col in df.columns for col in cols):
                raise ValueError(f'Missing columns in dataset. Required: {cols}')
        
        # Convert categorical `Star color` to numerical
        df['Star color'] = df['Star color'].astype('category').cat.codes

        # label and input features
        X = df[['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
                'Absolute magnitude(Mv)', 'Star type', 'Star color']].values
        y = df['Spectral Class'].values


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

        # Train and evaluate
        model = KNNClassifier(k= 3)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)

        print(f'Accuracy: {accuracy:.3f}')
        joblib.dump(model, 'trained_model.pkl')
