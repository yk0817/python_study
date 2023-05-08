def check_parentheses(s):
		stack = []
		for c in s:
			if c == "(":
				stack.append(c)
			elif c == ")":
				if len(stack) == 0:
					return False
				stack.pop()
		return len(stack) == 0