from linkers.setup_links import *
# from os import system
# from sys import argv,stdout
# import csv
# directory='/home/arka/Documents/1VACATION/Learn/links/HTML'
# link=''
# file=0
# #an empty reusable file variable

# def syntax_error () :
# 	print('''
#         *Wrong syntax!
#         for more options try [help] [-h] or [--help]
# ''')
# 	quit()
# 	return
def build_html(html_name,interaction):
	from os.path import expanduser
	home = expanduser("~")
	message=''
	exec(interaction)
	system(f'links.sh {html_name} "{message}"')
	return

# def manipulate_data(entry,statement):#newdata
# 	global file
# 	try:
# 		if int(input('Are you sure you want to delete this link?\n 1-yes\t0-no\n:')) is not 0:
# 			directory='/home/arka/Documents/1VACATION/Learn/links/HTML/frame/data/'
# 			if file is 0:
# 				link=f'{path}/links_main.csv'
# 			elif file is 1:
# 				link=f'{path}/ngos_main.csv'
# 			with open(link,'r') as f :
# 				data=f.read()
# 			count=0
# 			newdata=''
# 			for item in data.splitlines() :
# 				count+=1
# 				item+='\n'
# 				if count is entry:
# 					exec(statement)
# 				else:
# 					newdata+=item
# 			with open(link,'w') as f:
# 				f.write(newdata)
# 			update_exit()
# 		else:
# 			quit()
# 	except:
# 		print('Try again!')
# 		quit()
def file_not_found():
	print("This operation can't be completed because the file doesn't exist")
	if input("Manage file?    [Yes/No]").lower() in ['y','yes'] :
		pass # function call
	quit()

def set_link(html_name):
	global compendium,directory
	html_name=html_name.lower()
	try:
		if html_name in compendium:
			html_name=fetch_data(name=html_name,fetchname=True)
			html_link=f'{directory}/HTML/{html_name}.html'
	except:
		file_not_found()
	return html_link

# def update_exit():
# 	interaction=r'''
# if int(input('Do you want to write a message to your save?\n 1-yes, 0-no\n')) is not 0:
# 	message=input('Write your message:')
# '''
# 	build_html(interaction=interaction)

def build_exit(html_name):
	interaction=''
	build_html(html_name.lower(),interaction=interaction)
	
# def set_data(hyperlink,text):
# 	global file
# 	directory='/home/arka/Documents/1VACATION/Learn/links/HTML/frame/data/'
# 	if file is 0:
# 		link=f'{directory}/links_main.csv'
# 	elif file is 1:
# 		link=f'{directory}/ngos_main.csv'
# 	with open(link,'a') as f :
# 		f.write(f'{hyperlink}|{text}\n')
# 	update_exit()

# def delete_data(entry):#create gui
# 	# entry=list(map(int,entry))
# 	# entry=list(entry)
# 	manipulate_data(entry=entry,statement='continue')
# # 	#read+ file again, skip the count line and append bottom and artificially add EOF to the end 
# def add_data(entry,hyperlink,text):
# 	manipulate_data(entry=entry,statement=f'newdata+={hyperlink}|{text}')
# def help_intro(call = 'lref') :
# 	print(f'''

# ''')	
# 	return
