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
