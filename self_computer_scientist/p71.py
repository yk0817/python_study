def binary_search(a_list, n):
	first = 0
	last = len(a_list) - 1
	while last >= first:
		mid = (first + last) // 2
		if a_list[mid] == n:
			return True
		elif a_list[mid] > n:
			last = mid - 1
		else:
			first = mid + 1
