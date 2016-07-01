from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


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
