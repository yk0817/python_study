import string


def cipher(a_string, key):
	uppercase = string.ascii_uppercase
	lowercase = string.ascii_lowercase
	encoded = ""
	for char in a_string:
		if char in uppercase:
			encoded += uppercase[(uppercase.index(char) + key) % 26]
		elif char in lowercase:
			encoded += lowercase[(lowercase.index(char) + key) % 26]
		else:
			encoded += char
	return encoded

print(cipher("Hello World!", 3))