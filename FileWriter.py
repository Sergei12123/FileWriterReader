import json
import codecs
import xml.etree.ElementTree as ET
import FileReader
import Person
import os
import zipfile
import tkinter.filedialog as fd
import tkinter as tk


def txt_writer(context):
	f = open('file.txt', 'w', encoding='utf-8')
	print('Файл file.txt записан')
	f.write(context)
	f.close()


def json_writer(name, age, father, mother):
	person = Person.Person()
	person.name = name
	person.age = age
	person.parents = []
	person.parents.append(Person.Person())
	person.parents[0].role = "Father"
	person.parents[0].name = father
	person.parents.append(Person.Person())
	person.parents[1].role = "Mother"
	person.parents[1].name = mother
	with open('data.json', 'w', encoding='utf-8') as f:
		f.write(person.toJSON())
	print('Файл data.json записан')


def xml_writer(name, age, father, mother):
	# tree = FileReader.xml_reader()
	person = ET.Element('person')
	xname = ET.SubElement(person, 'name')
	xage = ET.SubElement(person, 'age')
	parents = ET.SubElement(person, 'parents')
	xfather = ET.SubElement(parents, 'father')
	fatherName = ET.SubElement(xfather, 'name')
	xmother = ET.SubElement(parents, 'mother')
	motherName = ET.SubElement(xmother, 'name')

	xname.text = name
	xage.text = age
	motherName.text = mother
	fatherName.text = father

	file = open('file.xml', 'w', encoding='utf-16')
	file.write(ET.tostring(person, encoding='unicode'))

def zip_writer(files):

	with zipfile.ZipFile('archive.zip', 'w') as myzip:
		for file in files:
			myzip.write(file.rsplit('/', 1)[1])


# zip_writer()
