#!/usr/bin/python

"""
Run FOSSology and Ninka and return their results. This file is for internal use
only and is called by dual_scan.py.

@author Doug Richardson
@author Jon von Kampen
@author James Thompson

@license Apache License 2.0
"""

import subprocess
import sys
import os
from signal import signal, SIGPIPE, SIG_DFL

import paths

NINKA_PATH = paths.NINKA_PATH + paths.NINKA
NOMOS_PATH = paths.FOSSOLOGY_AGENT_PATH + paths.NOMOS
FOSSOLOGY_WEB_PATH = paths.FOSSOLOGY_WEB_HOST + paths.WEB_NOMOS_SCAN

"""
The following FOSSology components can be accessed:
 - nomos: The license scanner
 - copyright: Scans for its nakesake
 - ununpack: Unpacks an ISO, tar, or other archive into component files
 - pkgagent: Scans package headers in RPMs and Debian packages listed on the
   command line
 - mimetype: Returns file types for files listed on the command line

Paths to these are included in paths.py in case they are desired for future
development.
"""

def ninka_scan(target):
    """Scans a file with Ninka."""
    nfile_name = target + ".ninka_out.txt"

    n_output = subprocess.check_output(
        [NINKA_PATH, '-d', target],
        preexec_fn = lambda: signal(SIGPIPE, SIG_DFL)
    )
    #preexec part added because of extraneous 'cat: broken pipe' errors

    return n_output

def foss_scan(target):
    """Scans a file with FOSSology by calling Nomos."""
    nomos = NOMOS_PATH
    f = False
    
    """
    Nomos returns a nonzero exit value by default.  This causes
    subprocess.check to throw an exception and the program to crash. The only
    way around it seemed to be to use exception handling.
    """
    try:
        f = subprocess.check_output([nomos, target])
    except Exception, e:
        f = str(e.output)
    
    return f
