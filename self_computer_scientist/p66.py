def linear_search(a_list, n):
	for i in a_list:
		if i == n:
			return True
	return False

a_list = [1, 8, 31, 101, 3, 23, 4, 12]
print(linear_search(a_list, 22))