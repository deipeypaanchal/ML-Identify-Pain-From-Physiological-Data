# This file contains the function to load data from a csv file.

import csv                      # Import the csv module to read csv files

def load_data(file_path):
    """
    Load data from a csv file.

    Args:
        file_path (str): The path to the csv file.

    Returns:
        list: A list of lists containing the data from the csv file. Each inner list represents a row in the csv file, 
              where the first three elements are the subject_id, data_type, and classifier, and the remaining elements 
              are the values.

    """
    # Initialize an empty list to store the data
    csv_data = []
    # Open the csv file in read mode
    with open(file_path, 'r') as file:
        # Create a csv reader object
        reader = csv.reader(file)
        # Iterate over each row in the csv file
        for row in reader:
            # Extract the subject_id, data_type, classifier, and values from the row
            subject_id, data_type, classifier = row[0], row[1], row[2]
            # Convert the values to a list of floats
            values = []
            # Iterate over the remaining elements in the row and convert them to floats
            for x in row[3:]:
                # Append the float value to the values list
                values.append(float(x))
            # Append the subject_id, data_type, classifier, and values to the csv_data list
            csv_data.append([subject_id, data_type, classifier, values])
    # Return the list of data
    return csv_data