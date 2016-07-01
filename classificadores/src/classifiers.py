from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm as SVM


def knn(k , X_train , y_train , X_test):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    classes = classifier.predict(X_test)
    return classes



def lda(X_train , y_train , X_test):
    lda_classifier = LinearDiscriminantAnalysis()
    lda_classifier.fit(X_train , y_train)
    classes = lda_classifier.predict(X_test)
    return classes

def svm(X_train , y_train , X_test):
    svm_classifier = SVM.SVC()
    svm_classifier.fit(X_train , y_train)
    classes = svm_classifier.predict(X_test)
    return classes
