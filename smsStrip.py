#@author b6938236 for InventedLife
#@date 2013.07.13
#
# Strip data from XML SMS

import io,os,os.path

directory  = 'PATH TO DIRECTORY'
output = open('log.txt','w')

for file in os.listdir(directory):
	f = open(directory + file,'r')
	data = ["NUM","DATE","MSG"]
	for line in f.readlines():
		if "FROM-TO-ADDR" in line:
			data[0] = line[24:-26]
		elif "RCVD-DATE-TIME" in line:
			data[1] = line[26:-28]
		elif "SMS-MESSAGE-BODY" in line:
			data[2] = line[24:-25]
	output.writelines("From: {}\n".format(data[0]))
	output.writelines("Date: {}\n".format(data[1]))
	output.writelines("Message: {}\n".format(data[2]))
	output.writelines("-----\n")
	output.writelines("\n")
	
output.close()
