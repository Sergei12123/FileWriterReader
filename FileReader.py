import json
import xml.etree.ElementTree as ET
import os


def txt_reader():
	if os.path.isfile('file.txt'):
		f = open('file.txt', 'r', encoding='utf-8')
		return f.read()
	else:
		return 'Файл file.txt не существует'


def json_reader():
	with open('data.json', 'r', encoding='utf-8') as file:
		data = file.read()
		return data


def xml_reader():
	data = ET.parse('file.xml')
	return data

# xml_reader()
