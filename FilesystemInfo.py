import os, string
import psutil


def get_drivers_info():
	d = psutil.disk_partitions()
	drivers_info = ''
	d = psutil.disk_partitions()
	for i in d:
		drivers_info += "Название:" + i[0]
		drivers_info += "\nFSTYPE: " + i[2]
		drivers_info += "\nOPTS: " + i[3]
		drivers_info += "\nВсего места: " + str(psutil.disk_usage(i[0])[0]) + "байт или " + str(int(psutil.disk_usage(i[0])[0]) / 1073741824) + " ГБ"
		drivers_info += "\nВсего свободного места: " + str(psutil.disk_usage(i[0])[2]) + "байт или " + str(int(psutil.disk_usage(i[0])[2]) / 1073741824) + " ГБ"
		drivers_info += "\n-----------------------------\n"
	return drivers_info
