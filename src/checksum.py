#!/usr/bin/python

"""
This method finds the SHA-1 checksum of a given file

@author Doug Richardson
@author Jon Von Kampen
@author James Thompson

@License Apache License 2.0

_hash_file and _hash _string originally written by Corbin Haughawout 
for the do_spdx project, used with permission.

(all comments in the functions are from the do_spdx project as well and
are left "as is")
"""

def _hash_file(file_path):
    '''
    A location independent checksum generator that generates a sha1
    of the contents of the file provided. Used in Do_SPDX to 
    provide a so-called PackageVerificationCode so that the user
    may detect if a package already has SPDX generated for it.
    '''
    with open(file_path, 'rb') as f:
        data_string = f.read()
        sha1 = _hash_string(data_string)
    return sha1

def _hash_string(data):
    '''
    This hashing function accepts some data as a string and runs it through
    the sha1 hashing algorithm. Returns the hexdigest of the data to the caller.
    This function is called from within the private _hash_file 
    method of the Do_SPDX module.
    '''
    from hashlib import sha1
    file_sha1 = sha1()
    file_sha1.update(data)
    return file_sha1.hexdigest()
