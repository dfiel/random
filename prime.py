#@author b6938236
#@date 2013.07.11
#
#Calculates prime numbers and save to text file.
#Resumes from last found prime in file.

import io,sys
file = io.open("prime.txt","r")
line = file.readline()
lastLine=line
while line != "":
	lastLine = line
	line = file.readline()
print("Starting from {}".format(lastLine))
file.close()
file = io.open("prime.txt","a")

def isPrime(n):
	if n % 2 == 0:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

n = int(lastLine) + 1
while True:
	if isPrime(n):
		file.writelines("{}\n".format(n))
		#print("Found prime at {}".format(n))
	n+=1
