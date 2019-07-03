from jinja2 import Environment, FileSystemLoader, select_autoescape
from sys import argv
from setup_links import *
from colorama import Fore,Back,Style
# to enable basic autoescape to avoid accidental intervention of code with string use
# autoesccape=select_autoescape(['html', 'xml'])
#followlinks=True to follow symbolic links...
env=Environment(
    loader=FileSystemLoader([f'{directory}/HTML/frame'],followlinks=True),
    autoescape=False
)#environment ready
#global in scope
try:
	if len(argv) is 2:
		if argv[1].lower() in compendium:
			data=fetch_data(argv[1].lower())
except:
	print(Style.BRIGHT+Back.RED+Fore.WHITE+'Invalid name!!'+Style.RESET_ALL)
	quit()
htmlname,title,icon,css,heading,main,footer_h,footer=data
link=f'{directory}/HTML/{htmlname}.html'
# to get template from env,
template=env.get_template('links_frame.html')##common to both ngos and link refer
#modifying html to the rendered template 
buffer=template.render(title=title,
icon=icon,
css=css,
heading=heading,
lists=main,
footer_heading=footer_h,
footer_text=footer)
#DRY in action
with open(link,'w') as f:
	f.write(buffer)
print(Style.BRIGHT+Fore.GREEN +u'\u2713\tFile has built successfully!!')
print(Fore.BLUE+f'''\tFollow the link to visit Webpage(Ctrl+click):
	\x1b]8;;file:///{link}\a'''+'\033[05mLINK TO WEBPAGE\x1b]8;;\a'+Style.RESET_ALL)