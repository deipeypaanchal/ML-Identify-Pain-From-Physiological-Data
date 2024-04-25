# ML-Pain-Classification-System-Using-Physiological-Data
This project involves developing a system that classifies pain from physiological data collected from wearable devices. The system processes data such as Diastolic BP, Systolic BP, EDA (Electrodermal Activity), and Respiration to identify patterns related to pain and no-pain conditions.

# Libraries used in this project
- NumPy
- csv
- Scikit-learn
    * sklearn.model_selection
    * sklearn.metrics
    * sklearn.ensemble
- Matplotlib
- os
- sys

# To run the project

- with venv already included: .venv/bin/python3 Project2.py <Data_Type> <Data_File>

Below is a template for the README file for your affective computing project on classifying pain from physiological data collected via wearable devices. This template provides a structured way to document your project, making it easier for others to understand and run your code.

## Usage
To run the script, use the following command:
```
python Project2.py <data_type> <data_file>
```
Where:
- `<data_type>` is one of 'dia', 'sys', 'eda', 'res', or 'all'.
- `<data_file>` is the absolute path to the CSV data file.

### Example
```
python Project2.py all /path/to/data.csv
```

## Features
- **Data Types Processed**: Diastolic BP, Systolic BP, EDA, Respiration
- **Feature Engineering**: Calculation of mean, variance, minimum, and maximum for each data type.
- **Classification**: Customizable classifier to determine pain presence.
- **Validation**: Uses 10-fold cross-validation to assess model performance.

## Outputs
- **Confusion Matrix**: Aggregated and averaged over 10 folds.
- **Classification Metrics**: Accuracy, precision, and recall, averaged over all folds.