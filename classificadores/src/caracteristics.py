import os
from os.path import isfile, join

def extrai_caracteristicas(nome_imagem):
	cmd = "./ProjetoIBM " + nome_imagem
	result = os.system(cmd)
	if result != 0:
		print('ERRO NA EXTRACAO DE CARACTERISTICAS !!!')
		exit
	else:
		return result

def extrai_caracteristicas_treina(diretorio , nome_imagem):
	cmd = "./ProjetoIBM " + diretorio + " " + nome_imagem
	result = os.system(cmd)
	if result != 0:
		print('ERRO NA EXTRACAO DE CARACTERISTICAS !!!')
		exit
	else:
		return result

def cross_extraction(bases_path , valid_base_name):
	dirs = [dir for dir in os.listdir(bases_path) if not isfile(join(bases_path , dir))]
	dirs.remove(valid_base_name)
	contador = 0
	result_files = []

	while contador < len(dirs):
		result_file_name = dirs[contador] + '_t' + str(contador) + '.txt'
		result_files.append(result_file_name)
		cmd = "./ProjetoIBM " + str(bases_path + dirs[contador] + '/') + " " + result_file_name
		result = os.system(cmd)
		contador += 1

	cmd = "./ProjetoIBM " + str(bases_path + valid_base_name + '/') + " valid.txt"
	result = os.system(cmd)

	train_file = open('train.txt' , 'w')
	contador = 0

	for file_name in result_files:
		temporary_file = open(result_files[contador] , 'r')
		for line in temporary_file:
			train_file.write(line)
		temporary_file.close()
		contador += 1

	train_file.close()

	for file_name in result_files:
		cmd = "rm " + file_name
		result = os.system(cmd)


def resultados(y_validacao , classes):
	contador = 0
	acertos = 0
	erros = 0
	while contador < len(y_validacao):
		if y_validacao[contador] == classes[contador]:
			acertos += 1
		else:
			erros += 1
		contador += 1
	print('acertos : ' + str(acertos))
	print('erros : ' + str(erros))
	print('taxa de reconhecimento : %.2f' % (acertos / len(classes)))
