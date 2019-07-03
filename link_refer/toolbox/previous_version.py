from os import system
from sys import argv,stdout
import csv
directory='/home/arka/Documents/1VACATION/Learn/links/HTML'
link=''
file=0 
#an empty reusable file variable

def syntax_error () :
	print('''
        *Wrong syntax!
        for more options try [help] [-h] or [--help]
''')
	quit()
	return
def build_html(interaction):
	global file
	message='.'
	exec(interaction)
	if file is 0 :
		system(f'~/link_refer/lref_tools/links.sh links "{message}"')
	elif file is 1 :
		system(f'~/link_refer/lref_tools/links.sh ngos "{message}"')
	return

def manipulate_data(entry,statement):#newdata
	global file
	try:
		if int(input('Are you sure you want to delete this link?\n 1-yes\t0-no\n:')) is not 0:
			directory='/home/arka/Documents/1VACATION/Learn/links/HTML/frame/data/'
			if file is 0:
				link=f'{directory}/links_main.csv'
			elif file is 1:
				link=f'{directory}/ngos_main.csv'
			with open(link,'r') as f :
				data=f.read()
			count=0
			newdata=''
			for item in data.splitlines() :
				count+=1
				item+='\n'
				if count is entry:
					exec(statement)
				else:
					newdata+=item
			with open(link,'w') as f:
				f.write(newdata)
			update_exit()
		else:
			quit()
	except:
		print('Try again!')
		quit()
def set_link(mode):
	global link, directory, file
	try:
		if argv[2].lower() == 'links' :
			link=f'{directory}/Links.html'
			file=0
		elif argv[2].lower() == 'ngos' :
			link=f'{directory}/NGOs.html'
			file=1
		return [link,file]#use unpacking the list
	except:
		exec(f'{mode}_help()')
		quit()
		
# convert help into a class and import later
def update_exit():
	interaction=r'''
if int(input('Do you want to write a message to your save?\n 1-yes, 0-no\n')) is not 0:
	message=input('Write your message:')
'''
	build_html(interaction=interaction)

def build_exit():
	interaction=''
	build_html(interaction=interaction)
	
def set_data(hyperlink,text):
	global file
	directory='/home/arka/Documents/1VACATION/Learn/links/HTML/frame/data/'
	if file is 0:
		link=f'{directory}/links_main.csv'
	elif file is 1:
		link=f'{directory}/ngos_main.csv'
	with open(link,'a') as f :
		f.write(f'{hyperlink}|{text}\n')
	update_exit()
def delete_data(entry):#create gui
	# entry=list(map(int,entry))
	# entry=list(entry)
	manipulate_data(entry=entry,statement='continue')
# 	#read+ file again, skip the count line and append bottom and artificially add EOF to the end 
def add_data(entry,hyperlink,text):
	manipulate_data(entry=entry,statement=f'newdata+={hyperlink}|{text}')
def help_intro(call = 'lref') :
	print(f'''

''')	
	return
def convert_pdf_help(call = 'lref') :
	print(f'**CONVERT to pdf and store     :   {call} convert-link ')	#2
	return
def edit_help(call = 'lref') :
	print(f'**open to EDIT in sublime/gedit:   {call} edit   [filename] [gedit]\n  --default is sublime--')	#3,4
	return
def add_help(call = 'lref') :
	print(f"**ADD new url at position      :   {call} add    [filename] [serial number] -u '[url]' -m '[hyperlink text]'")	#8
	return
def append_help(call = 'lref') :
	print(f"**APPEND new url               :   {call} append [filename]  -u '[url]' -m '[hyperlink text]'")	#7
	return
def view_help(call = 'lref') :
	print(f"**VIEW the html files          :   {call} view   [filename]")	#3
	return
def delete_help(call = 'lref') :
	print(f"**DELETE an entry              :   {call} delete [filename] [serial number]")	#4
	return
def help (call = 'lref') :
	help_intro()
	convert_pdf_help()
	edit_help()
	view_help()
	append_help()
	add_help()
	delete_help()
	print()
	quit()
	return 

#!/usr/bin/python3
import sys, os, csv
from sys import argv
from tools.lref_functions import *  
import click
#system of checks to ensure correct input and also to handle all cases
#if help is found anywhere, we'll help 1st
#If a global variable is pulled inside a function is manipulated, then the true global value remaiins unchanged
#Hence there can be no pointer operations on any function /object /class etc.
def main():
'''


*This is a small program that manipulates a fed in html files, in specific ways 
*[Add code by ~code~] into the hyperlink text
*Also [filename] is:
	"links" for "Links.html"
	"ngos" for "NGOs.html"
*text editors supported [application name]: 
	'gedit(for Ubuntu text editor)'  &  'subl(for Sublime Text)[default]' 

'''
#end of docstring
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