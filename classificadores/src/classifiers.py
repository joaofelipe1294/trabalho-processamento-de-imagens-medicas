from sklearn.neighbors import KNeighborsClassifier


def knn(k , X_train , y_train , X_test):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    classes = classifier.predict(X_test)
    return classes
