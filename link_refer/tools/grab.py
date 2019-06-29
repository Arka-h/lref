#!/usr/bin/python3.7
##What I learned :
#reversed(string) produces an iteratable object whereas string [::-1] produces a reversed string object
#also that it's not from sys import sys.argv, but it's from sys import argv ...not sys.argv as argv
from os import system
from sys import argv
string = ''
for char in reversed(argv[1]) :
	if(char is '/') :
		break
	string+=char
var=string[::-1]
print(var)