from sys import argv
from functions import *
from caracteristics import *
from classifiers import *
from results import *

argc = len(argv)
if argc == 1:
	show_help()

elif argc == 2:
	X_train , y_train = get_train_data()
	X_valid , y_valid = get_validation_data()

	if argv[1] == 'knn':
		k = 3
		classes = knn(k , X_train , y_train , X_valid)

	elif argv[1] == 'lda':
		classes = lda(X_train , y_train , X_valid)

	elif argv[1] == 'svm':
		classes = svm(X_train , y_train , X_valid)

	elif argv[1] == 'all':
		recognition_rates = []
		k = 3
		classes = knn(k , X_train , y_train , X_valid)
		recognition_rates.append(recognition_rate(y_valid , classes))
		classes = lda(X_train , y_train , X_valid)
		recognition_rates.append(recognition_rate(y_valid , classes))
		classes = svm(X_train , y_train , X_valid)
		recognition_rates.append(recognition_rate(y_valid , classes))
		show_recognition_rates(recognition_rates)
		exit()

	show_results(y_valid , classes)

elif argc == 3 and argv[1] == 'knn':
	k = int(argv[2])
	X , y = get_train_data()
	X_valid , y_valid = get_validation_data()
	classes = knn(k , X , y , X_valid)
	show_results(y_valid , classes)

elif argc == 3:
	cross_extraction(argv[1] , argv[2])
	print('Caracteristicas extraidas , execute novamente com um classificador selecionado !')

elif (argc > 3 and argc < 6) and argv[1] == '-c' :
	X_train , y_train = get_train_data()
	X_valid , y_valid = get_validation_data()
	if argc == 4:
		classifiers = [argv[2] , argv[3]]
	else:
		classifiers = [argv[2] , argv[3] , argv[4]]

	probabilities = []
	for classifier in classifiers:
		if classifier == 'knn':
			k = 3
			probabilities.append(knn_probabilities(k , X_train , y_train , X_valid))
		elif classifier == 'lda':
			probabilities.append(lda_probabilities(X_train , y_train , X_valid))
		elif classifier == 'svm':
			probabilities.append(svm_probabilities(X_train ,y_train , X_valid))

	index = 0
	iterations = len(probabilities[0])
	classes = []
	while index < iterations:
		pathologic = 0
		non_pathological = 0
		counter = 0
		while counter < len(probabilities):
			non_pathological += probabilities[counter][index][0]
			pathologic += probabilities[counter][index][1]
			counter += 1
		if pathologic > non_pathological:
			classes.append(1)
		elif non_pathological > pathologic:
			classes.append(0)
		index += 1
	show_results(y_valid , classes)
