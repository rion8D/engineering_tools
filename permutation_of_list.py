def permutation_of_list(l, size):
	n = len(l)
	out_list = []
	for num_10 in range(n**size):
		index_list = []
		while num_10:
			if num_10%n>=10:
				return -1
			index_list.append(num_10%n)
			num_10 //= n
		for _ in range(size-len(index_list)):
			index_list.append(0)

		out_list.append([l[i] for i in index_list])
	
	return out_list

if __name__ == '__main__':
	l = ['a','b','c']
	print(rekkyo(l, 4))
