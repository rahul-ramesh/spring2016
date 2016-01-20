#!/usr/bin/python

from __future__ import print_function
import sys

def question2():
	#Get path from command line argument
	path = str(sys.argv[1])

	#Get text from the file
	arr = readfile(path)
	
	#separate the words
	text = arr.split(" ")
	
	#Get frequency distribution of words
	freqs = getFreq(text)

	#format for printing to stdout
	output = ""
	for word in sorted(freqs, reverse=True):
		output = output + (word + ":" + str(freqs[word]) + ",")
	
	print (output[0:-1], end="")

#Given a path, this returns first line
def readfile(path):
	f = open(path)
	lines = f.readline().rstrip()
	f.close()
	return lines


#Given a list of words, this returns a dict with frequency distribution.
def getFreq(words):
	d = {}
	for word in words:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
	return d

question2()
