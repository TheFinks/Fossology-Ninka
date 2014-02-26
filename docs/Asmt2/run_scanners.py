#!/usr/bin/python

import subprocess
import sys
import os
import paths
import tarfile
import zipfile

#This program is licensed under GPLv2 or any newer version
#This program is created by Doug Richardson

#NINKA_PATH = "/usr/share/ninka/ninka-1.1/ninka.pl"
NINKA_PATH = paths.NINKA_PATH + paths.NINKA
#FOSSOLOGY_PATH = "/usr/lib/fossology/agents/"
#NOMOS_PATH = "/usr/lib/fossology/agents/nomos"
NOMOS_PATH = paths.FOSSOLOGY_AGENT_PATH + paths.NOMOS
#FOSSOLOGY_WEB_PATH = "http://127.0.0.1/repo/?mod=agent_nomos_once"
FOSSOLOGY_WEB_PATH = paths.FOSSOLOGY_WEB_HOST + paths.WEB_NOMOS_SCAN

#the following things can be accessed within fossology
#nomos: the license scanner
#copyright: scans for its nakesake
#ununpack: unpacks an iso, tar, or other archive into component files
#pkgagent: scans package headers in RPM's and debian packages...
#...listed on the command line
#mimetype: returns file types for files listed on the command line

def ninka_scan(target):
	#TODO: create code for archive scanning

	cleanup1 = target + ".sentences"
	cleanup2 = target + ".license"
	nfile_name = target + ".ninka_out.txt"
	#ninka_string = NINKA_PATH + " -d " + sys.argv[1]

	#nfile = open(nfile_name, 'w')

	n_output = subprocess.check_output([NINKA_PATH, '-d', sys.argv[1]])
	subprocess.call(["rm", cleanup1])
	subprocess.call(["rm", cleanup2])
	#os.system(ninka_string) #if you use this, comment out the subprocess
		#...calls and file writing
	#nfile.close()

	return n_output

def foss_scan(target):
	#ffile_name = target + ".foss_out.txt"
	nomos = NOMOS_PATH
	#copyright_scanner = FOSSOLOGY_PATH + "copyright"
	#wget_string = "wget -qO - --post-file " + sys.argv[1]
	#wget_string += " " + FOSSOLOGY_WEB_PATH + " > " + ffile_name
	#nomos_string = nomos + " " + sys.argv[1]
	#ffile = open(ffile_name, 'w')
	f = False
	try:
		f = subprocess.check_output([nomos, sys.argv[1]])
	except Exception, e:
		#print("WARNING: nomos exited with a nonzero exit code")
		f = str(e.output)
	
	#nomos returns a nonzero kill value, throws an exception
	#os.system(wget_string)
	#os.system(nomos_string) #only nomos or wget is needed for fossology
		#...not both
	#ffile.close()
	
	return f

if len(sys.argv) < 2:
	print("USAGE: " + sys.argv[0] + " file")
	print("EXAMPLE: " + sys.argv[0] + " ninka.pl")

else:
	#if tarfile.is_tarfile(sys.argv[1]):
		#archive = tarfile.open(sys.argv[1], r)
		#for member in archive.getmembers():
			
	print(ninka_scan(sys.argv[1]))
	print(foss_scan(sys.argv[1]))
