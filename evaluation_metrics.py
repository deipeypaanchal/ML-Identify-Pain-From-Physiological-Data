import os
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

def PrintEvalMetrics(pred, indices, y,  data_type, fold_index):
    final_preds = []
    ground_truth_data = []

    for p in pred:
        final_preds.extend(p)
    for i in indices:
        ground_truth_data.extend(y[i])
    cm = confusion_matrix(final_preds, ground_truth_data)
    precision = precision_score(ground_truth_data, final_preds, average = 'macro')
    recall = recall_score(ground_truth_data, final_preds, average = 'macro')
    accuracy = accuracy_score(ground_truth_data, final_preds)
    new_dir = 'Final_Results_2/'
    os.makedirs(new_dir, exist_ok=True)
    file_name = data_type + ".txt"
    try:
        with open(os.path.join(new_dir, file_name), 'a') as file:
            file.write('Fold ' + str(fold_index)+'\n')
            file.write("\tConfusion matrix: "+str(cm) + '\n')
            file.write("\tPrecision: " + str(precision) + '\n')
            file.write("\tRecall: " + str(recall) + '\n')
            file.write("\tAccuracy: " + str(accuracy) + '\n')
    except Exception as e:
        print("File writing Error", e)
    return cm, precision, recall, accuracy