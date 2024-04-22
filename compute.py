# This file contains the function to compute the mean, variance, min, and max of the data.

import numpy as np      # Importing numpy to use numerical operations

# Compute the mean, variance, min, and max of the data for each data type
def compute_features(csv_data, data_type):
    """
    Compute the mean, variance, min, and max of the data.

    Parameters:
    csv_data (list): A list of tuples containing the data.
    data_type (str): The type of data to compute features for. Can be "dia", "sys", "eda", "res", or "all".

    Returns:
    tuple: A tuple containing three elements - features, labels, and subjects.
        - features (dict): A dictionary containing the computed features for each data type.
        - labels (list): A list of labels corresponding to the computed features.
        - subjects (list): A list of subject IDs corresponding to the computed features.
    """
    # Initialize empty lists to store the data types to be computed for each data type
    data_types_array = ["dia", "sys", "eda", "res"]
    # Initialize empty dictionary to store the data types to be computed for each data type
    data_array = {"dia": [], "sys": [], "eda": [], "res": []}
    # Iterate over the data types array to compute the data for each data type
    for type in data_types_array:
        # Filter the data based on the data type
        data_array[type] = [x for x in csv_data if type in x[1].lower()]
    # Initialize empty dictionaries to store the features, labels, and subjects for each data type
    features = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}
    labels = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}
    subjects = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}
    # Iterate over the data array to compute the features, labels, and subjects for each data type
    for type in data_array:
        # Iterate over the data in the data array
        data = data_array[type]
        # Iterate over the data to compute the features, labels, and subjects
        for subject_id, dtype, classifier, values in data:
            mean = np.mean(values)          # Compute the mean of the values using numpy
            variance = np.var(values)       # Compute the variance of the values using numpy
            min_value = np.min(values)      # Compute the minimum value of the values using numpy
            max_value = np.max(values)      # Compute the maximum value of the values using numpy
            feature = [mean, variance, min_value, max_value]        # Create a feature vector with mean, variance, min, and max
            features[type].append(feature)                          # Append the feature vector to the features list
            labels[type].append(classifier)                         # Append the classifier to the labels list
            subjects[type].append(subject_id)                       # Append the subject ID to the subjects list
    # Combine the features, labels, and subjects for all data types
    if data_type == "all":
        # Combine the features, labels, and subjects for all data types
        feature_length = len(features["dia"])
        # Iterate over the feature length to combine the features, labels, and subjects
        for i in range(feature_length):
            # Combine the features, labels, and subjects for all data types
            row = features["dia"][i] + features["sys"][i] + features["eda"][i] + features["res"][i]
            # Append the combined features to the "all" data type
            features["all"].append(row)
        # Update the labels and subjects for the "all" data type    
        labels["all"] = labels["dia"]
        # Update the subjects for the "all" data type
        subjects["all"] = subjects["dia"]
    # Return the features, labels, and subjects for the specified data type        
    return features, labels[data_type], subjects[data_type]