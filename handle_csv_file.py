import csv

def load_data(file_path):
    csv_data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            subject_id, data_type, classifier = row[0], row[1], row[2]
            values = []
            for x in row[3:]:
                values.append(float(x))
            csv_data.append([subject_id, data_type, classifier, values])
    return csv_data 