#!/usr/bin/python

#these are the paths to the files
#these were made on the system developed on, and may need to be changed...
#...for your system
NINKA_PATH = "/usr/share/ninka/ninka-1.1/"
FOSSOLOGY_AGENT_PATH = "/usr/lib/fossology/agents/"

#This is the route to the fossology web application for using wget
FOSSOLOGY_WEB_HOST = "127.0.1.1/repo/"

#Here are the names of the files utilized
#nomos, copyright, ununpack, pkgagent, and mimetype are fossology agetns
NINKA = "ninka.pl"
NOMOS = "nomos"
COPYRIGHT_SCANNER = "copyright"
UNUNPACK = "ununpack"
PKGAGENT = "pkgagent"
MINETYPE_SCANNER = "mimetype"

#Here are some options for command-line usage of fossology
WEB_NOMOS_SCAN = "?mod=agent_nomos_once"
WEB_COPYRIGHT_SCAN = "?mod=agent_copyright_once"

'''
	The archive path 
	will be created, then destroyed with 
	its contents once the scan is finished
'''
TEMP_ARCHIVE_UNPACK_PATH = "temp_archive"
'''
	The file path is assumed to be present and permanent
	The file or archive to be scanned will temporarily be placed there
	The file or archive will be destroyed after the scans are finished
'''
SCAN_TARGET_PATH = "scan_target"
SCANNER_OUTPUT_PATH = "scanner_output"
