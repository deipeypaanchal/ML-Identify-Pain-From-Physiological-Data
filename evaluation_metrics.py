# This file contains the code to evaluate the model using confusion matrix, precision, recall, and accuracy.

import os       # To use os for file operations
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score     # To use confusion_matrix, accuracy_score, precision_score, recall_score

def PrintEvalMetrics(pred, indices, y,  data_type, fold_index):
    """
    Print the evaluation metrics using confusion matrix, precision, recall, and accuracy scores for each fold and data type and write the results to a file.

    Parameters:
    pred (list): List of predicted labels for each fold.
    indices (list): List of indices for each fold.
    y (list): List of ground truth labels.
    data_type (str): Type of data being evaluated.
    fold_index (int): Index of the current fold.

    Returns:
    cm (array): Confusion matrix.
    precision (float): Precision score.
    recall (float): Recall score.
    accuracy (float): Accuracy score.
    """

    # Initialize empty lists to store the final predictions and ground truth data
    final_preds = []
    ground_truth_data = []
    # Using for loop to iterate over the predicted labels and indices
    for p in pred:
        # Extend the final predictions list with the predicted labels
        final_preds.extend(p)
    # Using for loop to iterate over the indices
    for i in indices:
        # Extend the ground truth data list with the ground truth labels
        ground_truth_data.extend(y[i])
    # Compute the confusion matrix using confusion_matrix function from sklearn metrics
    cm = confusion_matrix(final_preds, ground_truth_data)
    # Compute the precision score with macro averaging using precision_score function from sklearn metrics
    precision = precision_score(ground_truth_data, final_preds, average='macro')
    # Compute the recall score with macro averaging using recall_score function from sklearn metrics
    recall = recall_score(ground_truth_data, final_preds, average='macro')
    # Compute the accuracy score using accuracy_score function from sklearn metrics
    accuracy = accuracy_score(ground_truth_data, final_preds)
    # Write the evaluation metrics to a file
    new_dir = 'Results_10Folds/'
    # Create a new directory if it does not exist
    os.makedirs(new_dir, exist_ok=True)
    # Create a file name based on the data type
    file_name = data_type + ".txt"
    # Try writing the evaluation metrics to a file
    try:
        # Open the file in append mode
        with open(os.path.join(new_dir, file_name), 'a') as file:
            file.write('Fold ' + str(fold_index) + '\n')                # Write the fold index to the file
            file.write("\tConfusion matrix: " + str(cm) + '\n')         # Write the confusion matrix to the file
            file.write("\tPrecision: " + str(precision) + '\n')         # Write the precision score to the file
            file.write("\tRecall: " + str(recall) + '\n')               # Write the recall score to the file
            file.write("\tAccuracy: " + str(accuracy) + '\n')           # Write the accuracy score to the file
    # Handle any exceptions that occur while writing to the file
    except Exception as e:
        # Print an error message if an exception occurs
        print("File writing Error", e)
    # Return the evaluation metrics
    return cm, precision, recall, accuracy