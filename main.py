from tkinter import *
import os
import FileReader
import FileWriter
import FilesystemInfo
import tkinter.filedialog as fd


def readTxt():
	output.configure(text="Текст из файла:\n" + FileReader.txt_reader())


def writeTxt():
	FileWriter.txt_writer(txtEntry.get())


def writeJson():
	FileWriter.json_writer(nameEntry.get(), ageEntry.get(), fatherNameEntry.get(),
	                       motherNameEntry.get())


def readJson():
	output.configure(text="Текст из файла:\n" + FileReader.json_reader(), justify=LEFT)


def writeXml():
	FileWriter.xml_writer(nameEntry.get(), ageEntry.get(), fatherNameEntry.get(),
	                      motherNameEntry.get())


def readXml():
	if os.path.isfile('file.xml'):
		data = 'Person\n'
		person = FileReader.xml_reader().getroot()
		data += "Name: " + person.find('name').text
		data += "\nAge: " + person.find('age').text
		data += "\nFather name: " + person.find('parents/father/name').text
		data += "\nMother name: " + person.find('parents/mother/name').text
		output.configure(text=data, justify=LEFT)
	else:
		output.configure(text='Файл file.xml не существует')


def packZip():
	filez = fd.askopenfilenames(parent=window, title='Choose a file')
	FileWriter.zip_writer(filez)


def systemInfo():
	output.configure(text=FilesystemInfo.get_drivers_info(), justify=LEFT)



window = Tk()
window.title("1 Практика")
window.geometry('900x600')

txtLbl = Label(window, text="2 задание (.txt)")
txtLbl.grid(column=0, row=0)
txtContentLbl = Label(window, text="Содержание")
txtContentLbl.grid(column=1, row=0)
txtEntry = StringVar()
txt = Entry(window, width=30, textvariable=txtEntry)
txt.grid(column=2, row=0)
btnTxtWrite = Button(window, text="Создать файл", command=writeTxt)
btnTxtWrite.grid(column=3, row=0)
btnTxtRead = Button(window, text="Прочитать из файла", command=readTxt)
btnTxtRead.grid(column=4, row=0)

jsonLbl = Label(window, text="3 задание (.json)")
jsonLbl.grid(column=0, row=2)

nameLbl = Label(window, text="Имя")
nameLbl.grid(column=1, row=2)
nameEntry = StringVar()
name = Entry(window, width=30, textvariable=nameEntry)
name.grid(column=2, row=2)

ageLbl = Label(window, text="Возраст")
ageLbl.grid(column=1, row=3)
ageEntry = StringVar()
age = Entry(window, width=30, textvariable=ageEntry)
age.grid(column=2, row=3)

fatherNameLbl = Label(window, text="Имя Отца")
fatherNameLbl.grid(column=1, row=4)
fatherNameEntry = StringVar()
fatherName = Entry(window, width=30, textvariable=fatherNameEntry)
fatherName.grid(column=2, row=4)

motherNameLbl = Label(window, text="Имя Матери")
motherNameLbl.grid(column=1, row=5)
motherNameEntry = StringVar()
motherName = Entry(window, width=30, textvariable=motherNameEntry)
motherName.grid(column=2, row=5)

btnJsonWrite = Button(window, text="Записать в файл json", command=writeJson)
btnJsonWrite.grid(column=3, row=5)
btnJsonRead = Button(window, text="Прочтитать из файла json", command=readJson)
btnJsonRead.grid(column=4, row=5)
btnJsonWrite = Button(window, text="Записать в файл xml", command=writeXml)
btnJsonWrite.grid(column=3, row=6)
btnJsonRead = Button(window, text="Прочтитать из файла xml", command=readXml)
btnJsonRead.grid(column=4, row=6)

xmlLbl = Label(window, text="4 задание (.zip)")
xmlLbl.grid(column=2, row=10)
btnxmlRead = Button(window, text="Создать архив", command=packZip)
btnxmlRead.grid(column=3, row=10)


btnxmlRead = Button(window, text="Смотреть информацию о дисках", command=systemInfo)
btnxmlRead.grid(column=3, row=12)

output = Label(window)
output.grid(column=2, row=15)

window.mainloop()
