from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm


def console_help():
	print('#SEM_TREINAMENTO -> python main.py imagem.tif id_classificador')
	print('#TREINAMENTO -> python main.py -t base_treinamento/ imagem.tif id_classificador')
	print('#VALIDACAO CRUZADA -> python main.py caminho/das/bases nome_base_validacao id_classificador')
	print('+-----------------+')
	print('| Classificadores |')
	print('+-----------------+')
	print('|   1-)   KNN 3   |')
	print('|   2-)   KNN 5   |')
	print('|   3-)   LDA     |')
	print('|   4-)   SVM     |')
	print('|   5-)   TODOS   |')
	print('+-----------------+')


def pega_valores():
	X = []
	y = []
	treinamento = open('results.txt' , 'r')
	for linha in treinamento:
		valores_str = linha.split(',')
		contador = 0
		lista = []
		while contador < len(valores_str) - 1:
			lista.append(int(valores_str[contador]))
			contador += 1
		X.append(lista)
		y.append(int(valores_str[len(valores_str) - 1][1]))
	return X , y

def dados_teste():
	arquivo = open('image.txt' , 'r')
	dados = arquivo.readline().split(',')
	X_teste = []
	values = []
	for valor in dados:
		values.append(int(valor))
	X_teste.append(values)
	return X_teste

def classifica(teste , classificador , X , y):
	if classificador == 1:
		neigh = KNeighborsClassifier(n_neighbors=3)
		neigh.fit(X, y)
		classe = neigh.predict(teste)
		return classe
	elif classificador == 2:
		neigh = KNeighborsClassifier(n_neighbors=5)
		neigh.fit(X, y)
		classe = neigh.predict(teste)
		return classe
	elif classificador == 3:
		lda_classifier = LinearDiscriminantAnalysis()
		lda_classifier.fit(X , y)
		classe = lda_classifier.predict(teste)
		return classe
	elif classificador == 4:
		svm_classifier = svm.SVC()
		svm_classifier.fit(X , y)
		classe = svm_classifier.predict(teste)
		return classe
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
