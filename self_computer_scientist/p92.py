def bubble_sort(a_list):
	loop_size = len(a_list) - 1
	for i in range(loop_size):
		for j in range(loop_size - i):
			if a_list[j] > a_list[j + 1]:
				a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
	return a_list

print(bubble_sort([1, 8, 31, 101, 3, 23, 4, 12]))