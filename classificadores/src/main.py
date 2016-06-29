from sys import argv
from functions import *


argc = len(argv)
if argc == 1:
	console_help()
	exit()
elif argc == 3:
	nome_imagem = argv[1]
	classificador = int(argv[2])
	extrai_caracteristicas(nome_imagem)
elif argc == 5 and argv[1] == '-t':
	diretorio = argv[2]
	nome_imagem = argv[3]
	classificador = int(argv[4])
	extrai_caracteristicas_treina(diretorio , nome_imagem)
X , y = pega_valores()
teste = dados_teste()
classe = classifica(teste , classificador , X , y)
print(classe)
