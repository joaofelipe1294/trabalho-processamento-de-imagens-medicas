import os


def extrai_caracteristicas(nome_imagem):
	cmd = "./ProjetoIBM " + nome_imagem
	result = os.system(cmd)
	if result != 0:
		print('ERRO NA EXTRACAO DE CARACTERISTICAS !!!')
		exit
	else:
		return result

def extrai_caracteristicas_treina(diretorio , nome_imagem):
	import os
	cmd = "./ProjetoIBM " + diretorio + " " + nome_imagem
	result = os.system(cmd)
	if result != 0:
		print('ERRO NA EXTRACAO DE CARACTERISTICAS !!!')
		exit
	else:
		return result
