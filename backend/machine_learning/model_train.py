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
import pickle

# Donart
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

    print_accuracy(y_train, y_train_predict, y_test, y_test_predict)

    """
    Save the model
    """
    filename = 'version6.0_svm_c_model.sav'
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
    filename = 'version1.0_mlp_c_model.sav'
    pickle.dump(mlp_clf, open(filename, 'wb'))


dataset=pd.read_csv("../FinalMixedPDF_Dataset.csv", encoding = 'unicode_escape')

dataset.dropna(inplace=True)

data=dataset.iloc[:,2:]
label=dataset.iloc[:,1]

print(label.value_counts())

X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=10)


svm_clf(X_train, y_train, X_test, y_test)
mlp_clf(X_train, y_train, X_test, y_test)

# #Pre-processing
# # from sklearn.feature_extraction.text import TfidfTransformer
# # transformer = TfidfTransformer(norm='l2',smooth_idf=True,use_idf=True)
# # X_train = transformer.fit_transform(X_train)
# # X_test=transformer.transform(X_test)
#
#
#
#
#
#
#
#
# #Naive Bayes
# from sklearn.naive_bayes import MultinomialNB
# mlt_nb = MultinomialNB().fit(X_train, y_train)
# y_train_pred = mlt_nb.predict(X_train)
# print("Naive Bayes")
# print(accuracy_score(y_train, y_train_pred))
#
#
#
#
# #CNN
# from keras.models import Sequential
# from keras.layers import Dense, Conv2D, Flatten
# #create model
# model = Sequential()
# #add model layers
# model.add(Conv2D(64, kernel_size=3, activation='relu'))
# model.add(Conv2D(32, kernel_size=3, activation='relu'))
# model.add(Flatten())
# model.add(Dense(10, activation='softmax'))
#
# #compile model using accuracy to measure model performance
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# #train the model
# # model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)
#
#
# from keras.layers import Input, Dense
# from keras.models import Model
#
# # This returns a tensor
# inputs = Input(shape=(784,))
#
# # a layer instance is callable on a tensor, and returns a tensor
# # output_1 = Dense(64, activation='relu')(X_train)
# # output_2 = Dense(64, activation='relu')(output_1)
# # predictions = Dense(10, activation='softmax')(output_2)
# #
# # # This creates a model that includes
# # # the Input layer and three Dense layers
# # model = Model(inputs=inputs, outputs=predictions)
# # model.compile(optimizer='rmsprop',
# #               loss='categorical_crossentropy',
# #               metrics=['accuracy'])
# # model.fit(data, labels)  # starts training