# ----------- File Handling -----------
import os
# Provides functions to interact with the operating system (e.g., file paths, directories)
import pickle
# Used for saving and loading Python objects (e.g., models, data structures)

# ----------- Image Processing (scikit-image) -----------
from skimage.io import imread  # Used to read images from disk into NumPy arrays
from skimage.transform import resize  # Used to resize images to a uniform shape

# ----------- Scientific Computing -----------
import numpy as np  # Provides support for numerical operations and handling arrays

# ----------- Machine Learning (scikit-learn) -----------
from sklearn.model_selection import train_test_split
# Splits data into training and testing sets
from sklearn.model_selection import GridSearchCV
# Performs hyperparameter tuning via grid search
from sklearn.svm import SVC
# Support Vector Classification model for supervised learning
from sklearn.metrics import accuracy_score
# Evaluates model performance by comparing predicted vs. actual labels


# prepare data
input_dir = r"C:\Users\Dell\Desktop\Setup\clf-data"
categories = ['empty', 'not_empty']

data = []
labels = []
for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# train classifier
classifier = SVC()

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_

y_prediction = best_estimator.predict(x_test)

score = accuracy_score(y_prediction, y_test)

print('{}% of samples were correctly classified'.format(str(score * 100)))

pickle.dump(best_estimator, open('model.p', 'wb'))