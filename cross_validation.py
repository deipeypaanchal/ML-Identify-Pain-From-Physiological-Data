from sklearn.model_selection import GroupKFold
from evaluation_metrics import PrintEvalMetrics

def subject_independent_cross_validation(X, y, clf, data_type, subjects):
    n_folds = 10
    groups = subjects

    gkf = GroupKFold(n_splits=n_folds)
    gkf.get_n_splits(X, y, groups)

    confusion_matrix_scores = []
    precision_scores = []
    recall_scores = []
    accuracy_scores = []

    for i in range(10):
        for fold_index, (train_index, test_index) in enumerate(gkf.split(X, y, groups)):
            if i == fold_index:
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y[train_index], y[test_index]

                clf.fit(X_train, y_train)
                pred = clf.predict(X_test)
                cm, precision, recall, accuracy = PrintEvalMetrics([pred], [test_index], y, data_type, fold_index + 1)

                confusion_matrix_scores.append(cm)
                precision_scores.append(precision)
                recall_scores.append(recall)
                accuracy_scores.append(accuracy)

    return confusion_matrix_scores, precision_scores, recall_scores, accuracy_scores