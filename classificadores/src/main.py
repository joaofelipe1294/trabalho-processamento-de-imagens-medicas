from sys import argv
from functions import *
from caracteristics import *
from classifiers import *
from results import *

argc = len(argv)
if argc == 2 and argv[1] == '-h':
	show_help()

elif argc == 2 and argv[1] == 'knn':
	k = 3
	X , y = get_train_data()
	X_valid , y_valid = get_validation_data()
	classes = knn(k , X , y , X_valid)
	show_results(y_valid , classes)

elif argc == 3 and argv[1] == 'knn':
	k = int(argv[2])
	X , y = get_train_data()
	X_valid , y_valid = get_validation_data()
	classes = knn(k , X , y , X_valid)
	show_results(y_valid , classes)

elif argc == 4:
	cross_extraction(argv[1] , argv[2])
	classificador = int(argv[3])
	X , y = pega_valores()
	X_validacao , y_validacao = dados_validacao()
	classes = classifica(X_validacao , classificador , X , y)
	resultados(y_validacao , classes)
#print(classes)
#print(y_validacao)
