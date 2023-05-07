def insertion_sort(a_list):
	for i in range(1, len(a_list)):
		value = a_list[i]
		j = i - 1
		while j >= 0 and value < a_list[j]:
			a_list[j + 1] = a_list[j]
			j -= 1
		a_list[j + 1] = value
	return a_list

print(insertion_sort([1, 8, 31, 101, 3, 23, 4, 12]))