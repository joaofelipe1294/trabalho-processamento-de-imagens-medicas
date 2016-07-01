def show_results(y_valid , classes):
	recognition = recognition_rate(y_valid , classes)
	print('taxa de reconhecimento : %.2f' % recognition)
	maze_matrix(y_valid , classes)


def recognition_rate(y_valid , classes):
	counter = 0
	hits = 0
	misses = 0
	while counter < len(y_valid):
		if y_valid[counter] == classes[counter]:
			hits += 1
		else:
			misses += 1
		counter += 1
	return hits / len(classes)


def maze_matrix(y_valid , classes):
	pathogenic = [0 , 0]
	non_pathogenic = [0 , 0]
	counter = 0
	while counter < len(y_valid):
		if y_valid[counter] == 0:
			if classes[counter] == 0:
				non_pathogenic[0] += 1
			elif classes[counter] == 1:
				non_pathogenic[1] += 1

		elif y_valid[counter] == 1:
			if classes[counter] == 0:
				pathogenic[0] += 1
			elif classes[counter] == 1:
				pathogenic[1] += 1

		counter += 1
	print('+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|' % (' ' * 10 , ' NEGATIVE ' , ' POSITIVE '))
	print('+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|' % (' NEGATIVE ' ,(' ' * 4 ) + str(non_pathogenic[0]) , (' ' * 4 ) + str(non_pathogenic[1])))
	print('+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|' % (' POSITIVE ' ,(' ' * 4 ) + str(pathogenic[0]) , (' ' * 4 ) + str(pathogenic[1])))
	print('+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10))



def show_recognition_rates(recognition_rates):
	print('+%-10s+%-10s+' % ('-' * 10 , '-' * 10))
	print('|%-10s|%-10s|' % (' KNN' , ' ' * 4 +  str(int(100 * recognition_rates[0]))))
	print('+%-10s+%-10s+' % ('-' * 10 , '-' * 10))
	print('|%-10s|%-10s|' % (' LDA ' ,(' ' * 4 ) + str(int(100 * recognition_rates[1]))))
	print('+%-10s+%-10s+' % ('-' * 10 , '-' * 10))
	print('|%-10s|%-10s|' % (' SVM ' ,(' ' * 4 ) + str(int(100 * recognition_rates[2]))))
	print('+%-10s+%-10s+' % ('-' * 10 , '-' * 10))
