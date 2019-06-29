#!/usr/bin/python3
from os import getcwd,environ
config=f'''[directory]
directory={getcwd()}

[webpages]
links:''
ngos:''
'''
with open(f"/home/{environ['USER']}/link_refer/config.ini",'w') as file:
	file.write(config)
print('Response recorded! File found!')