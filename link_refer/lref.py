#!/usr/bin/python3
import sys, os, csv
from sys import argv
from lref_tools.lref_functions import *  
#system of checks to ensure correct input and also to handle all cases
#if help is found anywhere, we'll help 1st
#If a global variable is pulled inside a function is manipulated, then the true global value remaiins unchanged
#Hence there can be no pointer operations on any function /object /class etc.
for i in argv :	
	if i == '--help'or i == 'help' :
		help()
#After checking for help we see if only filename is invoked,
#And urge the user to get help
###############################################################################################################
if len(argv) is 1 :
	syntax_error() 
###############################################################################################################
elif len(argv) is 2 :# convert-link # edit # view #
	# try:
	if argv[1] == 'convert-link': 
	#if user wants to convert to pdf 					
	#redirecting to py code
		os.system('python ~/Documents/1VACATION/Learn/HTML_to_PDF/html_to_pdf.py')
	elif argv[1]=='edit': 
		os.system("subl \"~/link_refer/lref.py\" \"~/link_refer/lref_tools/lref_functions.py\" ")
	elif argv[1]=='view':
		argv.append('links')
		link,file=set_link('view')
		build_exit()
	# except:
	# 	syntax_error()
###############################################################################################################
elif len(argv)is 3: # view # edit #
	try:
		if argv[1] == 'view' :#If user wants to view the html 
		#Setting up the link
			link,file=set_link('view')
			build_exit()
#End of view
		elif argv[1] == 'edit' :#If the user wants to edit the html
			print("\n\nDon't forget to COMMIT your changes on Git!...\n\n")
			link,file=set_link('edit')
			os.system(f'subl "{link}" "{directory}/frame/data/links_main.csv" "{directory}/frame/data/ngos_main.csv"')
			os.system(f'xdg-open "{directory}"')
	except:
		syntax_error()
###############################################################################################################
elif len(argv)is 4 :# edit #
	# try:
	if argv[1]=='edit' :
		link,file=set_link('edit')
		if argv[3] == 'gedit' :
			os.system(f'gedit \"{link}\" "{directory}/frame/data/links_main.csv" "{directory}/frame/data/ngos_main.csv"')
			os.system(f'xdg-open "{directory}"')
		elif argv[3] == 'subl' :
			os.system(f'subl \"{link}\" "{directory}/frame/data/links_main.csv" "{directory}/frame/data/ngos_main.csv"')
			os.system(f'xdg-open "{directory}"')
#End of edit
	elif argv[1]=='delete':
		link,file=set_link('delete')
		delete_data(int(argv[3]))

	# except:
	# 	syntax_error()
###############################################################################################################
elif len(argv)is 7:
	# try:
	if argv[1] =='append':
		link,file=set_link('append')
		if argv[3]=='-u':
			set_data(hyperlink=argv[4],text=argv[6])
		elif argv[3]=='-m':
			set_data(hyperlink=argv[6],text=argv[4])#order independent
	# except:
	# 	syntax_error()
###############################################################################################################
elif len(argv)is 8:
	try:
		if argv[1] =='add':
			link,file=set_link('add')
			if argv[4]=='-u':
				set_data(entry=int(argv[3]),hyperlink=argv[5],text=argv[7])
			elif argv[4]=='-m':
				set_data(entry=int(argv[3]),hyperlink=argv[7],text=argv[5])
	except:
		syntax_error()
#End of append
#End of program