import numpy as np
from collections import Counter
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import StandardScaler
from sklearn.utils.validation import check_X_y, check_array


'''
Building a classifier that Use temperature, luminosity, color_index, log_g as input to predict a star’s spectral class and stage on the HR.
Using the Euclidean distance: to compare the test star x_vector to neigbouring training stars,

K-Nearest Neighbors Classifier for Stellar Spectral Classification:
D = sqrt [(x1 - xi1)**2 + (x2 - xi2)**2 + ... (xn - xin)**2]
'''



class KNNClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, k= 5, distance_metric= 'euclidean'):
        self.k = k
        self.distance_metric = distance_metric
        self.scaler = StandardScaler()

    def fit(self, X, y):

        '''
        fit the classifier with the training data.

        Parameters: X and y

        Returns

        self : object
            Returns self.
                ''' 

        X, y = check_X_y(X, y)
        self.X_train_ = self.scaler.fit_transform(X)
        self.y_train_ = y
        return self

    def compute_distances(self, X):

        '''
        Compute distances between each xj test point and xi training points
        '''

        if self.distance_metric == 'euclidean':
            # L2 distance
            distance = np.sqrt(((self.X_train_[np.newaxis, :, :] - X[:, np.newaxis, :]) ** 2).sum(axis= 2))
        else:
            raise ValueError(f'Unsupported distance metric: {self.distance_metric}')
        return distance

    def predict(self, X):

        '''
        Predict the class labels for given data.

        Parameters: X features

        Returns
        y_pred class
        '''
        
        X = check_array(X)
        X_scaled = self.scaler.transform(X)
        distance = self.compute_distances(X_scaled)

        # For each row in test data
        y_pred = []

        for dist_row in distance:
            k_indices = np.argsort(dist_row)[:self.k]
            k_labels = self.y_train_[k_indices]
            most_common = Counter(k_labels).most_common(1)[0][0]
            y_pred.append(most_common)

        return np.array(y_pred)

    '''
    The metrics: using the sklearn to compute the score and the classification report
    '''

    def score(self, X, y):
        
        '''
        Return the accuracy score on the given test data and labels.
        Accuracy Score = Correct Predictions/Total_predictions

        '''

        from sklearn.metrics import accuracy_score
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)


    '''
        The perfomance:
    '''
