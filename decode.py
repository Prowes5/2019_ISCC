import base64


def decode(message):
	flag = ''
	s = base64.b64decode(message)
	for i in s:
		x = ord(i)-16
		x = x^32
		flag += chr(x)
	return flag

print decode('eYNzc2tjWV1gXFWPYGlTbQ==')