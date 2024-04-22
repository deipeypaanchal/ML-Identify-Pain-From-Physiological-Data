import sys
from handle_csv_file import load_data
from compute import compute_features
from evaluation import evaluate

def main():
    if len(sys.argv) != 3:
        print("Usage: python Project2.py <data_type> <data_file>")
        sys.exit(1)
    data_type = sys.argv[1]
    data_file = sys.argv[2]
    data = load_data(data_file)
    features, labels, subjects = compute_features(data, data_type)
    evaluate(features, labels, data_type, subjects)

if __name__ == "__main__":
    main()
    # box_plot(features)