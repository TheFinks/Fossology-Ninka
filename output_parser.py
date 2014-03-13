#!/usr/bin/python

import sys #for testing
import os #for testing

#default format is File myfile.c containes licence(s) L1, L2
def foss_parser(foss_in):
	foss_tokens = foss_in.split(" ")
	license = "F_ERROR" #If the file cannot be parsed
	file_name = "ERROR"
	
	#If it doesn't start with file, then nomos threw an error
	#The first license is on the 5th token

	#print("DEBUG: " + str(foss_tokens))

	if foss_tokens[0].strip() == 'File' and len(foss_tokens) > 4:
		for i in range(4, len(foss_tokens)):
			if license == "F_ERROR":
				license = foss_tokens[i]
			else:
				license += foss_tokens[i]
		file_name = foss_tokens[1]

	elif foss_tokens[0] == 'nomos:' and len (foss_tokens) > 2:
		temp = foss_tokens[2].split("/")
		file_name = temp[len(temp) - 1].replace("\"","")
		'''
			on non-files, nomos throws an error message
			in this message, the path is in quotes
		'''
		license = "ERROR"

	

	return (file_name, license)

#default format is file_name;license(s);[other stuff we don't need]
def ninka_parser(ninka_in):
	ninka_tokens = ninka_in.split(";")
	license = "F_ERROR"
	file_name = "ERROR"

	#print("DEBUG " + str(ninka_tokens))
	
	'''
		For our purposes we only need 2 things from ninkas output...
		...the file name and the confirmed license.
		The other things in it are ignored.

		The file is the first token and the license(s) is/are...
		...the second.

		The file is the absolute directory from the archive on downward.
		To compare it to fossology's output, we need to strip it...
		...down to the file name only.
	'''

	if len(ninka_tokens) > 1:
		license = ninka_tokens[1]
		temp = ninka_tokens[0].split("/")
		file_name = temp[len(temp) - 1]

	return (file_name, license)


'''
	This assumes ninkas input, since it retains the file path from...
	...the archive name on downward while nomos does not
'''
def file_path(ninka_in):
	output = "ERROR"
	tokens = ninka_in.split(";")
	if len (tokens) > 1:
		output = tokens[0]

	return output


#The next part is a command line based test to see the results

'''

if len(sys.argv) < 3:
	print("USAGE: " + sys.argv[0] + " fossology_file ninka_file")
	print("Example: " + sys.argv[0] + " ninka.pl.F_out.txt ninka.pl.N_out.txt")
	#print("If it is a ninka file, use the option -n")
	#print("Example: " + sys.argv[0] + " ninka.pl.N_out.txt -n")

elif not os.path.isfile(sys.argv[1]):
	print("ERROR: " + sys.argv[1] + " not found")

elif not os.path.isfile(sys.argv[2]):
	print("ERROR: " + sys.argv[2] + " not found")

	ARCHIVE = "busybox-1.22.1"
	foss = open(sys.argv[1], 'r')
	ninka = open(sys.argv[2], 'r')
	l1 = str(foss.read()).split("\n")
	l2 = str(ninka.read()).split("\n")
	#If not equal, go with the shortest one, will put in later
	if len(l1) == len(l2):
		for i in range(0, len(l1) - 1):
			foss_out = foss_parser(l1[i])
			ninka_out = ninka_parser(l2[i])
			if foss_out[0].strip() == ninka_out[0].strip():
				output = ARCHIVE + ";"
				output += foss_out[0].strip() + ";"
				output += foss_out[1] + ";"
				output += ninka_out[1]
				print(output)

	foss.close()
	ninka.close()
else:
	f = open(sys.argv[1], 'r')
	for line in f:
		print(ninka_parser(line))
	f.close()
'''
