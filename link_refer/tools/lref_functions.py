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


*This is a small program that manipulates a fed in html files, in specific ways 
*[Add code by ~code~] into the hyperlink text
*Also [filename] is:
	"links" for "Links.html"
	"ngos" for "NGOs.html"
*text editors supported [application name]: 
	'gedit(for Ubuntu text editor)'  &  'subl(for Sublime Text)[default]' 

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