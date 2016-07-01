from sys import argv
from functions import *
from caracteristics import *

argc = len(argv)
if argc == 1:
	console_help()
	exit()
elif argc == 2 and argv[1] == '-h':
	show_help()


	classificador = int(argv[1])
elif argc == 4:
	cross_extraction(argv[1] , argv[2])
	classificador = int(argv[3])
X , y = pega_valores()
X_validacao , y_validacao = dados_validacao()
classes = classifica(X_validacao , classificador , X , y)
resultados(y_validacao , classes)
#print(classes)
#print(y_validacao)
