def reverse_string(a_string):
	stack = []
	string = ""
	for char in a_string:
		stack.append(char)
	for _ in a_string:
		string += stack.pop()
	return string

print(reverse_string("Hello World!"))