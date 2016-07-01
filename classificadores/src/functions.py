from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm


def show_help():
	print('main.py knn # default k = 3')
	print('main.py knn k_value')
	exit()


def get_train_data():
	X = []
	y = []
	train = open('train.txt' , 'r')
	for line in train:
		values_str = line.split(',')
		count = 0
		list_temp = []
		while count < len(values_str) - 1:
			list_temp.append(int(values_str[count]))
			count += 1
		X.append(list_temp)
		y.append(int(values_str[len(values_str) - 1][1]))
	return X , y

def get_validation_data():
	arquivo = open('valid.txt' , 'r')
	X_validacao = []
	y_validacao = []
	for linha in arquivo:
		dados = linha.split(',')
		contador = 0
		caracteristicas = []
		while contador < len(dados) - 1:
			caracteristicas.append(int(dados[contador]))
			contador += 1
		X_validacao.append(caracteristicas)
		y_validacao.append(int(dados[len(dados) - 1]))
	return X_validacao , y_validacao


def classifica(teste , classificador , X , y):
	if classificador == 1:
		neigh = KNeighborsClassifier(n_neighbors=3)
		neigh.fit(X, y)
		classes = neigh.predict(teste)
		return classes
	elif classificador == 2:
		neigh = KNeighborsClassifier(n_neighbors=5)
		neigh.fit(X, y)
		classes = neigh.predict(teste)
		return classes
	elif classificador == 3:
		lda_classifier = LinearDiscriminantAnalysis()
		lda_classifier.fit(X , y)
		classes = lda_classifier.predict(teste)
		return classes
	elif classificador == 4:
		svm_classifier = svm.SVC()
		svm_classifier.fit(X , y)
		classes = svm_classifier.predict(teste)
		return classes
	elif classificador == 5:
		classes = []
		neigh = KNeighborsClassifier(n_neighbors=3)
		neigh.fit(X, y)
		classes.append(neigh.predict(teste)[0])
		neigh = KNeighborsClassifier(n_neighbors=5)
		neigh.fit(X, y)
		classes.append(neigh.predict(teste)[0])
		lda_classifier = LinearDiscriminantAnalysis()
		lda_classifier.fit(X , y)
		classes.append(lda_classifier.predict(teste)[0])
		svm_classifier = svm.SVC()
		svm_classifier.fit(X , y)
		classes.append(svm_classifier.predict(teste)[0])
		return classes
