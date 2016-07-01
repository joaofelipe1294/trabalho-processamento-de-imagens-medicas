def show_results(y_valid , classes):
	counter = 0
	hits = 0
	misses = 0
	while counter < len(y_valid):
		if y_valid[counter] == classes[counter]:
			hits += 1
		else:
			misses += 1
		counter += 1
	print('acertos : ' + str(hits))
	print('erros : ' + str(misses))
	print('taxa de reconhecimento : %.2f' % (hits / len(classes)))
	maze_matrix(y_valid , classes)



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
	print(non_pathogenic)
	print(pathogenic)
