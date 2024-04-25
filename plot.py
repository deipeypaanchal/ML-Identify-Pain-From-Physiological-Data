import matplotlib.pyplot as plt                     # Importing the matplotlib.pyplot module to plot the data
import numpy as np                                  # Importing the numpy module to use numerical operations        
from handle_csv_file import load_data               # Using load_data function from handle_csv_file module to load data from a file

def generate_boxplot(features):
    """
    Generate a box plot for the mean, variance, min, and max of the data.

    Parameters:
    features (dict): A dictionary containing the computed features for each data type.

    Returns:
    None
    """
    # Initialize empty lists to store the data
    mean = []                   # List to store the mean values
    variance = []               # List to store the variance values    
    min = []                    # List to store the min values      
    max = []                    # List to store the max values

    # Extract the features for each data type
    dia = features["dia"]                   # Extract the features for diastolic data
    eda = features["eda"]                   # Extract the features for EDA data
    sys = features["sys"]                   # Extract the features for systolic data
    res = features["res"]                   # Extract the features for respiration data
    # Combine the features for all data types into a single array
    data = np.concatenate((dia, eda, sys, res))
    # Extract the mean, variance, min, and max values
    mean = data[:, 0]                                   # Extract the mean values
    variance = data[:, 1]                               # Extract the variance values
    min = data[:, 2]                                    # Extract the min values
    max = data[:, 3]                                    # Extract the max values
    # Combine the mean, variance, min, and max values into a single list
    all_data = [mean, variance, min, max]               # Combine the mean, variance, min, and max values into a single list
    # Create a box plot for the mean, variance, min, and max values
    fig, ax = plt.subplots()
    # Create a box plot for the mean, variance, min, and max values
    ax.boxplot(all_data)
    # Set the labels for the x-axis to 'Mean', 'Variance', 'Min', and 'Max'
    ax.set_xticklabels(['Mean', 'Variance', 'Min', 'Max'])
    # Set the title of the plot to 'Box Plot of Mean, Variance, Min, and Max'
    ax.set_title('Box Plot of Mean, Variance, Min, and Max')
    # Show the plot        
    plt.show()

def plot_physiological_signals():
    """
    Plots the physiological signals from the loaded data.

    This function loads the data from a CSV file and plots the physiological signals.
    It retrieves the values for the first signal from the loaded data and plots them using matplotlib.

    Parameters:
        None

    Returns:
        None
    """
    # Load the data from the CSV file
    data = load_data('Project2Data.csv')

    # Extract the physiological signals from the loaded data
    # M007 Pain
    dia_values = data[292] 
    eda_values = data[293]
    sys_values = data[294]
    res_values = data[295]

    # Extract the signals from the data
    dia_signals = dia_values[3]
    eda_signals = eda_values[3]
    sys_signals = sys_values[3]
    res_signals = res_values[3]

    # plot the signals
    plt.figure(figsize=(10, 5))
    
    # Plot the physiological signals
    plt.plot(dia_signals, label='BP Dia_mmHg')
    plt.plot(eda_signals, label='EDA_microsiemens')
    plt.plot(sys_signals, label='LA Systolic BP_mmHg')
    plt.plot(res_signals, label='Respiration Rate_BPM')
    
    # Add a legend to the plot
    plt.legend()
    
    # Set the title of the plot
    plt.title('Physiological Signals')

    # Set the x-axis label
    plt.xlabel('Signal Index')

    # Set the y-axis label
    plt.ylabel('Signal Value')
    
    # Show the plot
    plt.show()