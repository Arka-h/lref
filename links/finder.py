import os
def exists(file):
	try:
		os.stat(file).st_size
		return True
	except:
		return False
def main():
	from os.path import expanduser
	home = expanduser("~")
	file=f"{home}/link_refer/toolbox/config.ini"
	if exists(file):
		buffer=''
		with open(file,'r') as f:
			buffer=f.read()
			list=buffer.split('\n')
			list[2]=f'directory={os.getcwd()}'
			buffer=''
			for item in list:
				buffer+=item+'\n'
			buffer=buffer[0:-1]
		with open(file,'w') as f:
			f.write(buffer)

	else:
		config=f'''
[directory]
directory={os.getcwd()}

[webpages]
links:''
ngos:''
'''	
		with open(file,'w')as f:
			f.write(config)
# 	else:
# 		


if __name__ == '__main__':
	main()
print('Response recorded! File found!')