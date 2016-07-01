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
	counter = 0
	result_files = []

	while counter < len(dirs):
		result_file_name = dirs[counter] + '_t' + str(counter) + '.txt'
		result_files.append(result_file_name)
		cmd = "./ProjetoIBM " + str(bases_path + dirs[counter] + '/') + " " + result_file_name
		result = os.system(cmd)
		counter += 1

	cmd = "./ProjetoIBM " + str(bases_path + valid_base_name + '/') + " valid.txt"
	result = os.system(cmd)

	train_file = open('train.txt' , 'w')
	counter = 0

	for file_name in result_files:
		temporary_file = open(result_files[counter] , 'r')
		for line in temporary_file:
			train_file.write(line)
		temporary_file.close()
		counter += 1

	train_file.close()

	for file_name in result_files:
		cmd = "rm " + file_name
		result = os.system(cmd)
