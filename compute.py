import numpy as np

# Compute mean, variance, min, max
def compute_features(csv_data, data_type):
    data_types_array = ["dia", "sys", "eda", "res"]
    data_array = {"dia": [], "sys": [], "eda": [], "res": []}
    for type in data_types_array:
        data_array[type] = [x for x in csv_data if type in x[1].lower()]

    features = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}
    labels = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}
    subjects = {"dia": [], "sys": [], "eda": [], "res": [], "all": []}

    for type in data_array:
        data = data_array[type]
        for subject_id, dtype, classifier, values in data:
            mean = np.mean(values)
            variance = np.var(values)
            min_value = np.min(values)
            max_value = np.max(values)
            feature = [mean, variance, min_value, max_value]
            features[type].append(feature)
            labels[type].append(classifier)
            subjects[type].append(subject_id)
    
    if data_type == "all":
        feature_length = len(features["dia"])
        for i in range(feature_length):
            row = features["dia"][i] + features["sys"][i] + features["eda"][i] + features["res"][i]
            features["all"].append(row)
        labels["all"] = labels["dia"]
        subjects["all"] = subjects["dia"]
    return features, labels[data_type], subjects[data_type]