import csv,click
from os import system
from lref_functions import *  
from edit.defaults import *
#system of checks to ensure correct input and also to handle all cases
#if help is found anywhere, we'll help 1st
#If a global variable is pulled inside a function is manipulated, then the true global value remaiins unchanged
#Hence there can be no pointer operations on any function /object /class etc.
@click.group()
def main():
	'''

	*This is a small program that manipulates and manages html files built by the developer, in certain ways (for now) 
	## Some of them are:
		[Add 'code-feel' by ~<text>~] into the hyperlink text
	
	'''
	#end of docstring
	pass
###############################################################
@main.command()                                               #
def pdf():                                                    #
	""" **CONVERT to pdf and store"""                         #
	print('Redirecting to HTML_to_PDF...')                    #
	system(f'python {directory}/HTML_to_PDF/html_to_pdf.py')  #
###############################################################
@main.command()
@click.argument('html-name',default=default_html,required=False)
@click.option('--shallow',is_flag=True,help="Doesn't build the whole webpage but shows it as it is")
def view(html_name,shallow):
	""" **VIEW your html files"""
	if shallow is True :
		html_link=set_link(html_name)
		system(f'browse file://{html_name}')
	else :
		build_exit(html_name)
	
#####################################################################################################################
@main.command()
@click.option('--editor',default='sublime',help=u'Editor options:\n\t\u2192 sublime\n\t\u2192 gedit\n\t\u2192 vscode')
@click.argument('site-name',default='lref',required=False)
def edit(site_name,editor):
	""" **open to EDIT in your preffered editor """
	pass

#####################################################################################################################
@main.command()
@click.option('-m',prompt='Enter HyperLink Text',help='Enter the hyperlink text to display on webpage')
@click.option('--link',prompt='Enter Your Link',help='Enter the link to add to webpage')
@click.option('--position',default=0,help='specify ONLY for a different position,other than at the top')
@click.argument('html-name',default=default_html,required=False)
def add(html_name,position,m,link):
	""" **ADD new url at new position or at the end"""
	pass

#####################################################################################################################
@main.command()
@click.option('--position',default=0,help='specify ONLY for a different position,other than at the bottom')
@click.option('--all',is_flag=True,help='NEVER use this option unless extremely necessary,\nit WILL DELETE ALL trace of data for your webpage ')
@click.argument('html-name',default=default_html,required=False)
def delete(html_name,position):
	"""**DELETE an entry, a group of entries, or entire html"""
	pass
#####################################################################################################################
@main.command()
@click.option('--file-dir',default=0,help='specify ONLY for a different position,other than at the bottom')
@click.option('--all',is_flag=True,help='\nIt will backup all of the data for your webpage ')
@click.argument('html-name',default=default_html,required=False)
def backup(html_name,file_dir,all):
	'''**Creates a BACKUP of html(s) at the specified location'''
	pass
	##UNDER CONSTRUCTION
####################################################################################################################
if __name__ == '__main__':
    main()