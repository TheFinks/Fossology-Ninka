#!/usr/bin/python

'''
    This software was developed by Doug Richardson, with the help of
    Jon von Kampen and James Thompson.  This software is licensed under
    the Apache 2.0 license.

    These are global path variables stored in one place for easy configuration
    Not all of these are currently used, but are left in there for future
    versions
'''

'''
    these are the paths to the files
    these were made on the system developed on, and may need to be changed...
    ...for your system
'''
NINKA_PATH = "/usr/share/ninka/ninka-1.1/"
FOSSOLOGY_AGENT_PATH = "/usr/lib/fossology/agents/"

#This is the route to the fossology web application for using wget
FOSSOLOGY_WEB_HOST = "127.0.1.1/repo/"
'''
    Here are the names of the files utilized
    nomos, copyright, ununpack, pkgagent, and mimetype are fossology agents
    
    currently, copyright, ununpack, pkgagent and mimetype are not used.
    However, they were included anyway incase future development warrants them.
'''
NINKA = "ninka.pl"
NOMOS = "nomos"
COPYRIGHT_SCANNER = "copyright"
UNUNPACK = "ununpack"
PKGAGENT = "pkgagent"
MINETYPE_SCANNER = "mimetype"

#Here are some options for command-line usage of fossology (the wget way)
WEB_NOMOS_SCAN = "?mod=agent_nomos_once"
WEB_COPYRIGHT_SCAN = "?mod=agent_copyright_once"

'''
    Currently, FINAL_OUTPUT_PATH is not used, but may be used in future
    versions.

    The directories created by TEMP_ARCHIVE_UNPACK_PATH and SCANNER_OUTPUT_PATH
    and all the files within them are destroyed once the process is finished.
'''

TEMP_ARCHIVE_UNPACK_PATH = "temp_archive" #where files are unpacked and scanend
SCANNER_OUTPUT_PATH = "scanner_output" #where the combined scanner output goes
FINAL_OUTPUT_PATH = "dual_scan_output" #where the final file will go

