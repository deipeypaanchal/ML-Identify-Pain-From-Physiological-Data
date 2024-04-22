# This file contains the implementation of the subject-independent cross-validation method.

from sklearn.model_selection import GroupKFold          # Importing GroupKFold from sklearn.model_selection to perform group k-fold cross-validation
from evaluation_metrics import PrintEvalMetrics         # Importing PrintEvalMetrics function from evaluation_metrics to print evaluation metrics

def subject_independent_cross_validation(X, y, clf, data_type, subjects):
    """
    Perform subject-independent cross-validation using GroupKFold and Random Forest Classifier.

    Parameters:
    X (array-like): The input features.
    y (array-like): The target labels.
    clf (object): The classifier object.
    data_type (str): The type of data being used.
    subjects (array-like): The subject labels.

    Returns:
    tuple: A tuple containing the confusion matrix scores, precision scores, recall scores, and accuracy scores.
    """
    # Initialize the number of folds for cross-validation to 10
    n_folds = 10
    # Assign the subject labels to groups for GroupKFold to perform subject-independent cross-validation
    groups = subjects
    # Initialize the GroupKFold object with 10 folds
    subjectIndependentKFold = GroupKFold(n_splits=n_folds)
    # Get the number of splits for the data
    subjectIndependentKFold.get_n_splits(X, y, groups)
    # Initialize empty lists to store the evaluation metrics
    confusion_matrix_scores = []    # List to store confusion matrix scores    
    precision_scores = []           # List to store precision scores
    recall_scores = []              # List to store recall scores
    accuracy_scores = []            # List to store accuracy scores
    # Using for loop to iterate over the number of folds
    for i in range(10):
        # Using for loop to iterate over the train and test indices
        for fold_index, (train_index, test_index) in enumerate(subjectIndependentKFold.split(X, y, groups)):
            # Check if the current fold index matches the fold index
            if i == fold_index:
                # Split the data into training and testing sets based on the indices
                X_train, X_test = X[train_index], X[test_index]                     # Split the input features into training and testing sets
                y_train, y_test = y[train_index], y[test_index]                     # Split the target labels into training and testing sets
                # Fit the classifier on the training data and predict the labels for the testing data
                clf.fit(X_train, y_train)
                # Predict the labels for the testing data
                pred = clf.predict(X_test)
                # Print the evaluation metrics for the current fold
                cm, precision, recall, accuracy = PrintEvalMetrics([pred], [test_index], y, data_type, fold_index + 1)
                # Append the evaluation metrics to the respective lists
                confusion_matrix_scores.append(cm)
                precision_scores.append(precision)
                recall_scores.append(recall)
                accuracy_scores.append(accuracy)
    # Return the evaluation metrics as a tuple 
    return confusion_matrix_scores, precision_scores, recall_scores, accuracy_scores