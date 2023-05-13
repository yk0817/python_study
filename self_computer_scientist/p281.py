def two_sum_brute(the_list, target):
	for i in range(0, len(the_list)):
		for j in range(i, len(the_list)):
			if the_list[i] + the_list[j] == target:
				return i, j

# print(two_sum_brute([1, 2, 3, 4, 5], 9))

def two_sum(a_list, target):
	a_dict = {}
	for index, n in enumerate(a_list):
		rem = target - n
		if rem in a_dict:
			return index, a_dict[rem]
		else:
			a_dict[n] = index
print(two_sum([1, 10, 3, 4, 5], 9))