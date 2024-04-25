# This script is the entry point of the program. It takes command line arguments, loads data from a file, computes features, and evaluates the model.
# Usage: python Project2.py <data_type> <data_file>

import sys                                          # Importing sys to use command line arguments to get data type and data file
from handle_csv_file import load_data               # Importing load_data function from handle_csv_file module to load data from a file
from compute import compute_features                # Importing compute_features function from compute module to compute features 
from evaluation import evaluate                     # Importing evaluate function from evaluation module to evaluate the model
from plot import generate_boxplot, plot_physiological_signals                   # Importing generate_boxplot function from plot module to generate boxplot

# Main function
def main():
    """
    Entry point of the program.
    
    This function takes command line arguments, loads data from a file, computes features, and evaluates the model.
    
    Usage: python Project2.py <data_type> <data_file>
    
    Parameters:
        data_type (str): Type of data to be processed.
        data_file (str): Path to the data file.
    """

    # Check if command line arguments are provided
    if len(sys.argv) != 3:
        # Print error message and exit program if not provided
        print("Usage: python Project2.py <data_type> <data_file>")
        sys.exit(1) # Exit program with error code 1
    # Get data type
    data_type = sys.argv[1]
    # Get data file path
    data_file = sys.argv[2]
    # Load data from data file
    data = load_data(data_file)
    # Compute features using data and data type
    features, labels, subjects = compute_features(data, data_type)
    # Evaluate the model using features, labels, data type, and subjects
    evaluate(features, labels, data_type, subjects)
    
    ############### TO PLOT THE BOXPLOT ###############
    # Generate boxplot for the features data
    # generate_boxplot(features)

# Call main function if script is executed
if __name__ == "__main__":
    ############# TO RUN THE MAIN FUNCTION #############
    main()
    
    ########### TO PLOT PHYSIOLOGICAL SIGNALS ###########
    # plot_physiological_signals()