#!/usr/bin/python3
# from html import unescape as convert ##If unescape is true in Jinja
import csv
class style():
	def __init__(self,htmlname,title,icon,css,heading,main,footer_h,footer_text):
		self.htmlname=htmlname
		self.title=title
		self.icon=icon
		self.css=css
		self.heading=heading
		self.main=main
		self.footer_h=footer_h
		self.footer_text=footer_text
		self.data=[self.htmlname,self.title,self.icon,self.css,self.heading,self.main,self.footer_h,self.footer_text]

def gather_content(name):
	main=[]
	footer=[]
	global path
	with open(f"{path}/main/{name}_main.csv") as link:
		f = csv.reader(link,delimiter='|') 
		counter=0;
		for row in f:
			counter+=1
			list_item=[f'{counter}.',row[0],row[1]]
			main.append(list_item)
	with open(f"{path}/footer/{name}_footer.csv") as link:
		f = csv.reader(link,delimiter='|') 
		for row in f: 
			list_item=row[0]
			footer.append(list_item)
	return main,footer

def get_config():
	from configparser import ConfigParser
	from os import environ
	config = ConfigParser()
	config.read(f"/home/{environ['USER']}/link_refer/config.ini")
	directory=config.get('directory','directory')
	temp=config.items('webpages')
	compendium=[]
	for name,x in temp:
		compendium.append(name)
	return directory,compendium

def execute_to_assemble(name):
	global main,footer
	buffer=''
	with open(f"{path}/details/{name}.csv",'r') as link:
		f=csv.reader(link,delimiter='|')
		link.readline()
		for row in f:
			buffer+=f'{row[0]}={row[1]},'
	buffer+='main=main,footer_text=footer'
	buffer=f'{name}=style({buffer})'
	return buffer
directory,compendium=get_config()
path=f'{directory}/HTML/frame/data'
if __name__ == '__main__':
	from pprint import pprint as p
	for name in compendium:
		main,footer=gather_content(name)
		exec(execute_to_assemble(name))
		exec(f'data={name}.data')
		p(data)
		print('\n\n\n')