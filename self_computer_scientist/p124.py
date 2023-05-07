def is_palindrome(s1):
	s1 = s1.replace(' ', '').lower()
	if s1 == s1[::-1]:
		return True
	return False

