def merge_sort(a_list):
	if a_list > 1:
		mid = len(a_list) // 2
		left = a_list[:mid]
		right = a_list[mid:]

		merge_sort(left)
		merge_sort(right)

		left_i = 0
		right_i= 0
		alias_i = 0
		while left_i < len(left) and right_i < len(right):
			if left[left_i] < right[right_i]:
				a_list[alias_i] = left[left_i]
				left_i += 1
			else:
				a_list[alias_i] = right[right_i]
				right_i+= 1
			alias_i += 1

		while left_i < len(left):
			a_list[alias_i] = left[left_i]
			left_i += 1
			alias_i += 1

		while right_i < len(right):
			a_list[alias_i] = right[right_i]
			right_i += 1
			alias_i += 1
	return a_list