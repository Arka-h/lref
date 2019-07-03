from setuptools import setup,find_packages
setup(
	name='link-refer',
	version='0.1',
	py_modules=['link_refer'],
	install_requires=[
	'Click','colorama','flask','pdfkit','jinja2'],
	entry_points='''
	[console_scripts]
	lref=link_refer:main
	''',
	# # metadata to display on PyPI
 #    author="Arka Haldi",
 #    author_email="aurkohaldi@gmail.com",
 #    description="This is a development stage Package to manage html files",
 #    url="https://github.com/Arka-h/lref",   # project home page, if any
 #    project_urls={
 #        "Documentation": "https://github.com/Arka-h/lref/blob/master/README.md",
 #        "Source Code": "https://github.com/Arka-h/lref",
 #    },
	)
