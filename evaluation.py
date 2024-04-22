from sklearn.ensemble import RandomForestClassifier
import numpy as np
from cross_validation import subject_independent_cross_validation
import os

def evaluate(X, y, data_type, subjects):
    X = X[data_type]
    X = np.array(X)
    y = np.array(y)
    subjects = np.array(subjects)

    classifier_RF = RandomForestClassifier()

    confusion_matrix_scores, precision_scores, recall_scores, accuracy_scores = subject_independent_cross_validation(X, y, classifier_RF, data_type, subjects)

    avg_confusion_matrix = np.mean((confusion_matrix_scores), axis=0)
    avg_precision = np.mean((precision_scores), axis=0)
    avg_recall = np.mean((recall_scores), axis=0)
    avg_accuracy = np.mean((accuracy_scores), axis=0)

    new_dir = 'Final_Results/'
    os.makedirs(new_dir, exist_ok=True)
    file_name = data_type + ".txt"
    try:
        with open(os.path.join(new_dir, file_name), 'a') as file:
            file.write('Average Scores \n')
            file.write("\tConfusion matrix: " + str(avg_confusion_matrix) + '\n')
            file.write("\tPrecision: " + str(avg_precision) + '\n')
            file.write("\tRecall: " + str(avg_recall) + '\n')
            file.write("\tAccuracy: " + str(avg_accuracy) + '\n')
    except Exception as e:
        print("Error while writing to file:", e)