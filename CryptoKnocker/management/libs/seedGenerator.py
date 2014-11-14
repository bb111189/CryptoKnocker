import string,random

def generateSeed(length = 16, chars = string.ascii_uppercase + "234567"):
	ret = ""
	for _ in range(length):	ret += random.choice(chars)
	return ret