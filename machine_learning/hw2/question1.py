#!/usr/bin/python

from __future__ import print_function
import sys

def question1():
	#Get path from command line argument
	path = str(sys.argv[1])

	#Get text from the file
	text = readfile(path)
	
	#Get list of unique words sorted in reverse order
	words = sorted(list(set(text.split(" "))), reverse=True)

	#format for printing to stdout
	output = ",".join(words)
	print (output, end= "")

#Given a path, this returns first line
def readfile(path):
	f = open(path)
	lines = f.readline().rstrip()
	f.close()
	return lines

question1()
