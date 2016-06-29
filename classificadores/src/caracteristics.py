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
		print("./ProjetoIBM " + str(bases_path + dirs[contador] + '/') + " " + result_file_name)
		cmd = "./ProjetoIBM " + str(bases_path + dirs[contador] + '/') + " " + result_file_name
		result = os.system(cmd)
		contador += 1
