#!/usr/bin/env python
import re
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

print ('Iniciando processamento\n')

def parse_xml():
	onlyfiles = [f for f in listdir('data') if isfile(join('data', f))]
	for f in onlyfiles:
		soup = BeautifulSoup(open(join('data',f)), "xml")
		print(soup.nomeservidor)

template_file = open("template/painelSRI_template.html",'r', encoding='utf-8')
psri_file = open("painel.html", 'w', encoding='utf-8')

lines = template_file.readlines()

for line in lines:
	matchobj = re.search('DATA', line)
	if matchobj:
		parse_xml()
		continue
	psri_file.write(line)




