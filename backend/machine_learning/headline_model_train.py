from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import CountVectorizer

import pickle


def print_accuracy(y_train, y_train_predict, y_test, y_test_predict, model_name="None"):
    """
    Testing the model
    """
    # Accuracy test
    print("==========================================")
    print("Accuracy Evaluation on ", model_name)
    print("Training data acc.", accuracy_score(y_train, y_train_predict))
    print("Testing data acc.", accuracy_score(y_test, y_test_predict))

    print("Training data confusion matrix:")
    print(confusion_matrix(y_train, y_train_predict, labels=[-1, 0, 1]))
    print("Training data precision macro", precision_score(y_train, y_train_predict, average="macro"))
    print("Training data precision weighted",precision_score(y_train, y_train_predict, average="weighted"))
    print("Training data recall macro",recall_score(y_train, y_train_predict, average="macro"))
    print("Training data recall wighted",recall_score(y_train, y_train_predict, average="weighted"))
    print("==========================================")

def svm_clf(X_train, y_train, X_test, y_test):
    svc_model = SVC(kernel="poly", degree=3, coef0=3, C=30, gamma="scale", random_state=10)

    trained_model = svc_model.fit(X_train, y_train)

    y_train_predict = trained_model.predict(X_train)
    y_test_predict = trained_model.predict(X_test)

    y_train_predict = cross_val_predict(trained_model, X_train, y_train, cv=3)
    # print(y_train_predict)

    print("SVM Classifier")
    print_accuracy(y_train, y_train_predict, y_test, y_test_predict)

    """
    Save the model
    """
    filename = 'version1.0_svm_c_model_headline.sav'
    pickle.dump(trained_model, open(filename, 'wb'))

def mlp_clf(X_train, y_train, X_test, y_test):
    # Training Neural Network
    from sklearn.neural_network import MLPClassifier

    mlp_clf = MLPClassifier(hidden_layer_sizes=(128, 64, 16), random_state=10, max_iter=1000)
    mlp_clf.fit(X_train, y_train)
    y_train_predict = mlp_clf.predict(X_train)
    y_test_predict=mlp_clf.predict(X_test)
    print("Neural Network")
    print_accuracy(y_train, y_train_predict, y_test, y_test_predict)

    """
        Save the model
        """
    filename = 'version1.0_mlp_c_model_headline.sav'
    pickle.dump(mlp_clf, open(filename, 'wb'))

def prepare_data():
    dataset = pd.read_excel("../headline_dataset.xlsx", encoding='utf_8_sig')
    dataset.dropna(inplace=True)
    X_train = dataset.Text
    label = dataset.Label
    #data = dataset.iloc[:, 3:]

    X_train, X_test, y_train, y_test = train_test_split(X_train, label, test_size=0.2, random_state=10)


    vect = CountVectorizer()
    vect.fit(X_train)
    vect_filename= 'version1.0_cv_model_headline.sav'
    pickle.dump(vect, open(vect_filename, 'wb'))

    X_train_dtm = vect.transform(X_train)
    X_test_dtm = vect.transform(X_test)

    X_train = X_train_dtm.toarray()
    X_test = X_test_dtm.toarray()

    return X_train, X_test, y_train, y_test

def train_models():
    X_train, X_test, y_train, y_test = prepare_data()

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    mlp = mlp_clf(X_train, y_train, X_test, y_test)
    svm = svm_clf(X_train, y_train, X_test, y_test)

train_models()