#!/usr/bin/env python3

"""
File path constants for internal use. These paths may need to be edited to
conform to the installation directories on your system. Not all are currently
in use; "extras" are anticipated to support upcoming features.

@author Doug Richardson
@author Jon von Kampen
@author James Thompson

@license Apache License 2.0
"""

NINKA_PATH = "/usr/share/ninka/ninka-1.1/"
FOSSOLOGY_AGENT_PATH = "/usr/lib/fossology/agents/"

FOSSOLOGY_WEB_HOST = "127.0.1.1/repo/"
"""URL of the FOSSology web application, for calling it via wget."""

"""
The following FOSSology components can be accessed:
 - nomos: The license scanner
 - copyright: Scans for its nakesake
 - ununpack: Unpacks an ISO, tar, or other archive into component files
 - pkgagent: Scans package headers in RPMs and Debian packages listed on the
   command line
 - mimetype: Returns file types for files listed on the command line
 
Currently, only nomos is used. The others are included in case they are desired
for future development.
"""

NINKA = "ninka.pl"
NOMOS = "nomos"
COPYRIGHT_SCANNER = "copyright"
UNUNPACK = "ununpack"
PKGAGENT = "pkgagent"
MINETYPE_SCANNER = "mimetype"

#Some options for command-line usage of FOSSology (the wget way)
WEB_NOMOS_SCAN = "?mod=agent_nomos_once"
WEB_COPYRIGHT_SCAN = "?mod=agent_copyright_once"

"""
The directories created by TEMP_ARCHIVE_UNPACK_PATH and SCANNER_OUTPUT_PATH
and all the files within them are destroyed once the process is finished.
"""
TEMP_ARCHIVE_UNPACK_PATH = "temp_archive"
"""Where files are unpacked and scanned."""
SCANNER_OUTPUT_PATH = "scanner_output"
"""Where the combined scanner output goes."""
FINAL_OUTPUT_PATH = "dual_scan_output"
"""
Where the final file will go. Currently not used but is anticipated for future
use.
"""
