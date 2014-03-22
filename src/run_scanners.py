#!/usr/bin/python

import subprocess
import sys
import os
import paths
from signal import signal, SIGPIPE, SIG_DFL

'''
    This software was developed by Doug Richardson, with the help of
    Jon von Kampen and James Thompson.  This software is licensed
    under the Apache 2.0 license.
'''
NINKA_PATH = paths.NINKA_PATH + paths.NINKA
NOMOS_PATH = paths.FOSSOLOGY_AGENT_PATH + paths.NOMOS
FOSSOLOGY_WEB_PATH = paths.FOSSOLOGY_WEB_HOST + paths.WEB_NOMOS_SCAN

'''
    the following things can be accessed within fossology
    nomos: the license scanner
    copyright: scans for its nakesake
    ununpack: unpacks an iso, tar, or other archive into component files
    pkgagent: scans package headers in RPM's and debian packages...
    ...listed on the command line
    mimetype: returns file types for files listed on the command line

    these are included in Paths.py if they are desired for future development
'''


def ninka_scan(target):

    nfile_name = target + ".ninka_out.txt"

    n_output = subprocess.check_output(
        [NINKA_PATH, '-d', target],
        preexec_fn = lambda: signal(SIGPIPE, SIG_DFL)
    )
    #preexec part added because of extraneous 'cat: broken pipe' errors

    return n_output

def foss_scan(target):
    nomos = NOMOS_PATH
    f = False
    '''
        Nomos returns a nonzero exit value by default.  This causes
        subprocess.check to throw an exception and the program to
        crash.  The only way around it seemed to be to exploit
        exception handling.
    '''
    try:
        f = subprocess.check_output([nomos, target])
    except Exception, e:
        f = str(e.output)
    
    return f
