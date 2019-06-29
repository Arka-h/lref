from jinja2 import Environment, FileSystemLoader, select_autoescape
from sys import argv
from linkers.setup_links import *
# to enable basic autoescape to avoid accidental intervention of code with string use
# autoesccape=select_autoescape(['html', 'xml'])
env=Environment(
    loader=FileSystemLoader(['./'],followlinks=True),#followlinks=True to follow symbolic links...
    autoescape=False
)#environment ready
print(directory,compendium)
#global in scope
# try:
if len(argv) is 2:
	if argv[1] in compendium:
		main,footer=gather_content(argv[1])
		exec(execute_to_assemble(argv[1]))
		exec(f'data={argv[1]}.data')
# except:
# 	print('syntax error')
# 	quit()
htmlname,title,icon,css,heading,main,footer_h,footer=data
link=f'{directory}/HTML/{htmlname}.html'
# to get template from env,
template=env.get_template('links_frame.html')##common to both ngos and link refer
#modifying html to the rendered template 
buffer=template.render(title=title,\
icon=icon,\
css=css,\
heading=heading,\
lists=main,\
footer_heading=footer_h,\
footer_text=footer)
#DRY in action
with open(link,'w') as f:
	f.write(buffer)
print('File has been successfully changed!!')
print(f'''Follow the link to visit Webpage(Ctrl+click):
	\x1b]8;;file:///{link}\aLINK TO WEBPAGE\x1b]8;;\a''')