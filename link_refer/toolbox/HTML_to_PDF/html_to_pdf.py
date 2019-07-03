import pdfkit
from sys import stdout
from time import sleep
from colorama import Fore,Back,Style
def Building_up_the_hype():
	while 1:
		text='Please wait'
		for i in range(3):
			text+='.'
			print(Fore.RED+text+Fore.RESET)
			sleep(1)
		print(' ')
		break
	return
def wwwcheck (link) :
	if link[0:4] == 'www.':
		flag=True
	else:
		flag=False
	return flag

#input starts here...

islink = input(Style.BRIGHT+Fore.GREEN+'''
Enter 0 if link is a file, or
1 if link is a website :    
'''+Style.RESET_ALL+Fore.BLUE)
link = input(Style.BRIGHT+Fore.GREEN+'Enter the link to be converted :'+Style.RESET_ALL+Fore.YELLOW+'[Example: www.google.com or /home/arka/../file.html]\n'+u'\u2B25 '+Fore.BLUE)
name = input(Style.BRIGHT+Fore.GREEN+'Enter name of the pdf file :'+Style.RESET_ALL+Fore.YELLOW+'  [Example: hyperlink text]    \n'+u'\u2B25 '+Fore.BLUE)

Building_up_the_hype()
# End of Input
options={'quiet':''}
if int(islink) is not 0 :#checks if its web link or not
	if wwwcheck(link) is True :#from site if 'www.' is used
		pdfkit.from_url('http://'+link, name+'.pdf')
	else :
		pdfkit.from_url(link, name + '.pdf')#from file
else :
	pdfkit.from_file('file://'+link, name + '.pdf')
print(Fore.RED+Style.BRIGHT+u'Done\u2713'+Style.RESET_ALL)
print()


'''
Usage of 

For simple tasks:

# import pdfkit

# pdfkit.from_url('http://google.com', 'out.pdf')
# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')

You can pass a list with multiple URLs or files:

# pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
# pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')

Also you can pass an opened file:

# with open('file.html') as f:
#     pdfkit.from_file(f, 'out.pdf')

If you wish to further process generated PDF, you can read it to a variable:

## Use False instead of output path to save pdf to a variable
# pdf = pdfkit.from_url('http://google.com', False)

You can specify all wkhtmltopdf options. 
You can drop '--' in option name. If option without value, use None, False or '' for dict value:
. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) 
you may use a list or a tuple. With option that need multiple values (e.g. --custom-header Authorization secret)
we may use a 2-tuple (see example below).

# options = {
#     'page-size': 'Letter',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'gzip')
#     ]
#     'cookie': [
#         ('cookie-name1', 'cookie-value1'),
#         ('cookie-name2', 'cookie-value2'),
#     ],
#     'no-outline': None
# }

# pdfkit.from_url('http://google.com', 'out.pdf', options=options)

By default, PDFKit will show all wkhtmltopdf output. If you don't want it, you need to pass quiet option:

# options = {
#     'quiet': ''
#     }

# pdfkit.from_url('google.com', 'out.pdf', options=options)

Due to wkhtmltopdf command syntax, TOC and Cover options must be specified separately. If you need cover before TOC, use cover_first option:

# toc = {
#     'xsl-style-sheet': 'toc.xsl'
# }

# cover = 'cover.html'

# pdfkit.from_file('file.html', options=options, toc=toc, cover=cover)
# pdfkit.from_file('file.html', options=options, toc=toc, cover=cover, cover_first=True)

You can specify external CSS files when converting files or strings using css option.

Warning This is a workaround for this bug in wkhtmltopdf. You should try --user-style-sheet option first.

# # Single CSS file
# css = 'example.css'
# pdfkit.from_file('file.html', options=options, css=css)

# # Multiple CSS files
# css = ['example.css', 'example2.css']
# pdfkit.from_file('file.html', options=options, css=css)

# You can also pass any options through meta tags in your HTML:

# body = """
#     <html>
#       <head>
#         <meta name="pdfkit-page-size" content="Legal"/>
#         <meta name="pdfkit-orientation" content="Landscape"/>
#       </head>
#       Hello World!
#       </html>
#     """

# pdfkit.from_string(body, 'out.pdf') #with --page-size=Legal and --orientation=Landscape

Configuration

Each API call takes an optional configuration paramater. This should be an instance of pdfkit.configuration() API call. It takes the configuration options as initial paramaters. The available options are:

    *wkhtmltopdf - the location of the wkhtmltopdf binary. By default pdfkit will attempt to locate this using which (on UNIX type systems) or where (on Windows).
    *meta_tag_prefix - the prefix for pdfkit specific meta tags - by default this is pdfkit-

Example - for when wkhtmltopdf is not on $PATH:

# config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
# pdfkit.from_string(html_string, output_file, configuration=config)'''



