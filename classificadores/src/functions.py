def show_help():
	print('main.py knn # default k = 3')
	print('main.py knn k_value')
	print('main.py lda')
	print('main.py svm')
	print('main.py all')
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
