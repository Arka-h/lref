# from html import unescape as convert ##If unescape is true in Jinja
########################################################################################################### # # # #
class style():
	def __init__(self,htmlname=False,title=False,icon=False,css=False,heading=False,main=False,footer_h=False,footer_text=False):
		self.htmlname=htmlname
		self.title=title
		self.icon=icon
		self.css=css
		self.heading=heading
		self.main=main
		self.footer_h=footer_h
		self.footer_text=footer_text
	def data(self):
		return [self.htmlname,self.title,self.icon,self.css,self.heading,self.main,self.footer_h,self.footer_text]
########################################################################################################### # # # #
def get_config():
	try:
		from configparser import ConfigParser
		from os import environ
		from os.path import expanduser
		home = expanduser("~")          #cross platform home
		config = ConfigParser()
		config.read(f"{home}/link_refer/toolbox/config.ini")
		directory=config.get('directory','directory')
		temp=config.items('webpages')
		compendium=[]
		for name,x in temp:
			compendium.append(name)
		path=f'{directory}/HTML/frame/data'
		return directory,compendium,path
	except:
		print('First run the finder.py to find location of htmls')
		quit()
########################################################################################################### # # # #

##############################################
directory,compendium,data_path=get_config()  #
##############################################

def gather_content(name):
	''' Gathers the main and footer content of the webpage'''
	import csv
	main=[]
	footer=[]
	global data_path
	with open(f"{data_path}/main/{name}_main.csv") as link:
		f = csv.reader(link,delimiter='|') 
		counter=0;
		for row in f:
			counter+=1
			list_item=[f'{counter}.',row[0],row[1]]
			main.append(list_item)
	with open(f"{data_path}/footer/{name}_footer.csv") as link:
		f = csv.reader(link,delimiter='|') 
		for row in f: 
			list_item=row[0]
			footer.append(list_item)
	return main,footer

def fetch_data(name,fetchname=False):
	'''must execute gather_content before running this,
	 prepares an executable buffer, which when executed,
	 fetches and assembles all the data about the page, in a list.'''
	if fetchname is False:
		import csv
		global data_path
		global directory
		main=[]
		footer=[]
		main,footer=gather_content(name)
		buffer=style()
		with open(f"{data_path}/details/{name}.csv",'r') as link:
			f=csv.reader(link,delimiter='|')
			link.readline()
			for row in f:
				exec(f"buffer.{row[0]}={row[1]}")
		buffer.main=main
		buffer.footer_text=footer
		buffer=buffer.data()#returns list
	elif fetchname is True:
		with open(f'{data_path}/details/{name}.csv','r')as f:
			f.readline()
			buffer=f.readline().split("'")[1]
	return buffer


#####################################
if __name__ == '__main__':          #
	from pprint import pprint as p  #
	for name in compendium:         #
		print(name)                 #
		data=fetch_data(name)       #
		p(data)                     #
		print('\n\n\n')             #
#####################################