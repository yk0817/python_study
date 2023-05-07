import string


def cipher(a_string, key):
	uppercase = string.ascii_uppercase
	lowercase = string.ascii_lowercase
	encrypto = ''

	for c in a_string:
		if c in uppercase:
			encrypto += uppercase[(uppercase.index(c) + key) % 26]
		elif c in lowercase:
			encrypto += lowercase[(lowercase.index(c) + key) % 26]
		else:
			encrypto += c
	return encrypto

print(cipher('Hello World', 3))