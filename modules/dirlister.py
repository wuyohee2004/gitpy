import os

def run(**args):
	print "[*] In dirlester module."
	files = os.listdir(".")
	return str(files)

