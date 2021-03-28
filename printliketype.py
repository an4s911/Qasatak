from random import randint
from time import sleep

def timeprint(string):
	"""
	This Function helps to print any string in a typing way
	As if someone is actually typing the content in the string in real time
	"""
	for i in string:
		print(i, end="")
		sleep(randint(1, 3)/randint(20,70))


