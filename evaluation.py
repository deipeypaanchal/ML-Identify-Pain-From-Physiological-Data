# This file contains the code to evaluate the model using Random Forest Classifier.

from sklearn.ensemble import RandomForestClassifier                     # To use Random Forest Classifier
import numpy as np                                                      # To use numpy for numerical operations               
from cross_validation import subject_independent_cross_validation       # To use subject_independent_cross_validation function
import os                                                               # To use os for file operations

# Evaluate the model using Random Forest Classifier
def evaluate(X, y, data_type, subjects):
    """
    Evaluate the model using Random Forest Classifier.

    Parameters:
    X (dict): A dictionary containing the input features.
    y (list): A list containing the target labels.
    data_type (str): The type of data being evaluated.
    subjects (list): A list containing the subject IDs.

    Returns:
    None
    """
    # Convert the input features and target labels to numpy arrays
    X = X[data_type]
    # Convert the input features to a numpy array
    X = np.array(X)
    # Convert the target labels to a numpy array
    y = np.array(y)
    # Convert the subject IDs to a numpy array
    subjects = np.array(subjects)
    # Initialize a Random Forest Classifier
    classifier_RF = RandomForestClassifier()
    # Perform subject-independent cross-validation using Random Forest Classifier and get the confusion matrix, precision, recall, and accuracy scores
    confusion_matrix_scores, precision_scores, recall_scores, accuracy_scores = subject_independent_cross_validation(X, y, classifier_RF, data_type, subjects)
    # Compute the average confusion matrix, precision, recall, and accuracy scores
    avg_confusion_matrix = np.mean((confusion_matrix_scores), axis=0)   # Compute the average confusion matrix with macro averaging and axis=0
    avg_precision = np.mean((precision_scores), axis=0)                 # Compute the average precision score with macro averaging and axis=0
    avg_recall = np.mean((recall_scores), axis=0)                       # Compute the average recall score with macro averaging and axis=0
    avg_accuracy = np.mean((accuracy_scores), axis=0)                   # Compute the average accuracy score with macro averaging and axis=0
    # Write the average scores to a file                
    new_dir = 'Results_Average/'
    # Create a new directory if it does not exist
    os.makedirs(new_dir, exist_ok=True)
    # Create a file name based on the data type
    file_name = data_type + ".txt"
    # Try writing the average scores to a file
    try:
        # Open the file in append mode
        with open(os.path.join(new_dir, file_name), 'a') as file:
            # Write the average scores to the file
            file.write('Average Scores \n')
            file.write("\tConfusion matrix: " + str(avg_confusion_matrix) + '\n')
            file.write("\tPrecision: " + str(avg_precision) + '\n')
            file.write("\tRecall: " + str(avg_recall) + '\n')
            file.write("\tAccuracy: " + str(avg_accuracy) + '\n')
    # Handle any exceptions that occur while writing to the file
    except Exception as e:
        # Print an error message if an exception occurs
        print("File writing error:", e)