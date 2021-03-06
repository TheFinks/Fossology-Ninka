#!/usr/bin/python

import paths
import sys
import os
import subprocess
import tarfile
import zipfile
import json
from run_scanners import ninka_scan, foss_scan
from output_parser import ninka_parser, foss_parser, combined_parser

'''
    This file was written by Doug Richardson and Jon von Kampen, with the help
    of James Thompson.

    This file is licensed under the Apache License, verison 2.0

    This file is the general script that runs the program proper
    It takes a file or archive, unpacks it (if applicable), and then
    subjects them to Fossology and Ninka scanners.  After which it creates
    a unified output file.  This file can be read and extrapolated from for
    whatever document is needed 

    (for this initial build, we made a JSON for the
    file-license portion of SPDX-1.2 for each file scanned).

    Future development notes (for those who wish to expand upon this).
    -May want to add a "percentage completed" (in factors of 10) for
    the archive scanner, as it can take a LONG time, and signs of progress
    would ease the user experience

    -May want to add an initial check method to see if NOMOS and Ninka
    are where files.py says they are (even if it's just checking if a file
    exists in that location).
'''

'''
    This trims down the absolute path so we can get the file name without
    extraneous directories
'''
def get_file_from_absolute_path(path_name):
    path_list = path_name.split("/")
    return path_list[len(path_list) - 1]

'''
    This is a subprocess that scans each file in an archive
    This function take advantage of the fact that tarfile and zipfile
    python packages have identical method names.
'''
def archive_scan(archive, scantype, f_name):
    #scan types can be n (ninka) or f (fossology)
    if not f_name:
        print("Error: Must specify an output file")
        archive.close()
        exit(1)
    else:
        f = open(f_name, 'w')
        for name in archive.getnames():
            path = paths.TEMP_ARCHIVE_UNPACK_PATH + "/" + name
            if scantype is 'n':
                f.write(ninka_scan(path))
            elif scantype is 'f':
                f.write(foss_scan(path))

#This gets rid of any internally used temporary directories if they remain
def clean():
    if os.path.isdir(paths.TEMP_ARCHIVE_UNPACK_PATH):
        subprocess.call(["rm", "-r", paths.TEMP_ARCHIVE_UNPACK_PATH])
    if os.path.isdir(paths.SCANNER_OUTPUT_PATH):
        subprocess.call(["rm", "-r", paths.SCANNER_OUTPUT_PATH])

'''
    Currently, this deletes a file with an identical name and location
    to one that this method will need to write to.
'''
def check_file(file_name):
    #an option to decide whether or not to overwrite may be added later
    if os.path.isfile(file_name):
        subprocess.call(["rm", file_name])

#This is the method that runs both scanners on a given file or package
def run_scans(target):

    print("creating directories needed for the scanners to work")

    '''
        Checks to see if the paths we need are there
        If they are not, it creates them

        (the archive path is meant for destruction, so it is assumed
        that it should not be there unless something went wrong)
    '''

    if not os.path.isdir(paths.SCANNER_OUTPUT_PATH):
        subprocess.call(["mkdir", paths.SCANNER_OUTPUT_PATH])
    if not os.path.isdir(paths.TEMP_ARCHIVE_UNPACK_PATH):
        subprocess.call(["mkdir", paths.TEMP_ARCHIVE_UNPACK_PATH])
    else:
        subprocess.call(["rm", paths.TEMP_ARCHIVE_UNPACK_PATH + "/*.*"])

    
    #To ensure the absolute path is not a part of the output file name
    out_name = get_file_from_absolute_path(target)

    ninka_out = paths.SCANNER_OUTPUT_PATH + "/"
    ninka_out += out_name + ".N_out.txt"
    check_file(ninka_out)
    foss_out = paths.SCANNER_OUTPUT_PATH + "/"
    foss_out += out_name + ".F_out.txt"
    check_file(foss_out)

    print("checking file format")

    if tarfile.is_tarfile(target):
        print(target + " identified as TAR file")
        archive = tarfile.open(target)
        print("extracting data")
        archive.extractall(paths.TEMP_ARCHIVE_UNPACK_PATH)
        print("starting ninka scan")
        archive_scan(archive, 'n', ninka_out)
        print("ninka scan finished")
        print("starting fossology scan")
        archive_scan(archive, 'f', foss_out)
        print("fossology scan finished")
        archive.close()

    #This is the same as the tarfile method but with zipfile
    elif zipfile.is_zipfile(target):    
        print(target + " identified as ZIP file")
        archive = zipfile.open(target)
        print("extracting data")
        archive.extractall(paths.TEMP_ARCHIVE_UNPACK_PATH)
        print("starting ninka scan")
        archive.scan(archive,'n', ninka_out)
        print("ninka scan finished")
        print("starting fossology scan")
        archive.scan(archive,'f', foss_out)
        print("fossology scan finished")
        archive.close()
    
    else: #assumes a single file
        print("file is either not an archive or an unrecognized format")
        path = paths.TEMP_ARCHIVE_UNPACK_PATH + "/" + target
        subprocess.call(["cp", target, paths.TEMP_ARCHIVE_UNPACK_PATH])
        #first with ninka
        n_file = open(ninka_out, 'w')
        print("starting ninka scan")
        n_file.write(ninka_scan(path))
        print("ninka scan fnished")
        n_file.close()

        #next with fossology
        f_file = open(foss_out, 'w')
        print("starting fossology scan")
        f_file.write(foss_scan(path))
        print("fossology scan finished")
        f_file.close()

    
    #clean()

    '''
    NOTE: Due to python limitations, this software currently...
    ...can NOT scan any other archive types.
    '''


'''
    This method parses the output of the Fossology and Ninka scans
    and places the result in a unified internal file.
'''
def parse_output(target, is_archive, foss_file, ninka_file):
    if not os.path.isfile(foss_file):
        print("ERROR: " + foss_file + " not found")
        exit(1)

    elif not os.path.isfile(ninka_file):
        print("ERROR: " + ninka_file + " not found")
        exit(1)
    else:

        out_name = get_file_from_absolute_path(target)
        print("Creating combined output file")
        combined_out = paths.SCANNER_OUTPUT_PATH + "/"
        combined_out += out_name + ".dual_out.txt"
        check_file(combined_out)

        if not is_archive:
            archive_name = "NONE"
        else:
            archive_name = out_name

        foss = open(foss_file, 'r')
        ninka = open(ninka_file, 'r')
        output_file = open(combined_out, 'w')
        l1 = str(foss.read()).split("\n")
        l2 = str(ninka.read()).split("\n")
        #If not equal, go with the shortest one, will put in later
        if len(l1) == len(l2):
            for i in range(0, len(l1) - 1):
                foss_out = foss_parser(l1[i])
                ninka_out = ninka_parser(l2[i])
                if foss_out[0].strip() == ninka_out[0].strip():
                    output = archive_name + ";"
                    output += foss_out[0].strip() + ";"
                    output += foss_out[1] + ";"
                    output += ninka_out[1] + "\n"
                    output_file.write(output)
                    

        foss.close()
        ninka.close()
        output_file.close()
        print("Output file complete")

'''
    This method parses the unified internal file that parse_output created
    and places the results in a tuple that can be easily translated to a
    JSON object for use with SPDX 1.2.

    The input format is archive_name;file_name;fossology_output;ninka_output

    The output format is (archive_name, file_name, license_declared, comments)
'''
def parse_combined_file(file_name):
    f = open(file_name, 'r')
    archive_name = "(ERROR)"
    file_name = "(ERROR)"
    license_declared = "(ERROR)"
    comments = "(ERROR)"
    output = False

    for line in f:
        file_info = line.split(";")
        archive_name = file_info[0] #The name of the archive scanned
        file_name = file_info[1] #The name of the file scanned
        foss_out = file_info[2].split(",") #Fossology's output
        ninka_out = file_info[3].split(",") #Ninka's output

        #If fossology and Ninka throw an error, skip this entry
        if foss_out[0] != "ERROR" and ninka_out[0] != "ERROR":
            result = combined_parser(foss_out, ninka_out)
            license_declared = result[0]
            comments = result[1]
            if not output:
                temp = (archive_name, file_name,
                    license_declared, comments)
                output = [temp]
            else:
                temp = (archive_name, file_name,
                    license_declared, comments)
                output.append(temp)
    
    return output

def generate_json(scan_list):
    """
    Generates a JSON string from a list of dual-scan results.
    
    Results are 4-tuples of the format:
        (package_name, file_name, license_concluded, comments)
    
    The JSON string is intended to be integrated into an overall SPDX document,
    as reflected by the key names. This function handles both single file and
    package scans.
    """
    
    results = {
        "package_name": "NONE",
        "file_results": {}
    }
    """
    package_name should be set other than "NONE" if more than one file is
    present, but it may be set if there is only one file that is part of a
    larger package.
    """
    for scan in scan_list:
        package_name = scan[0]
        file_name = scan[1]
        concluded = scan[2]
        comments = scan[3]
    
        if scan[0] != "NONE":
            results["package_name"] = package_name
        results["file_results"][file_name] = {
            "licenseConcluded": concluded,
            "licenseComments": comments
        }
    
    return json.dumps(results)

if len(sys.argv) < 2:
    print("USAGE: " + sys.argv[0] + " file")
    print("EXAMPLE: " + sys.argv[0] + " ninka.pl")

else:
    run_scans(sys.argv[1])
    out_name = get_file_from_absolute_path(str(sys.argv[1]))

    #Generate internal file names
    N_out = paths.SCANNER_OUTPUT_PATH + "/"
    N_out += out_name + ".N_out.txt"
    F_out = paths.SCANNER_OUTPUT_PATH + "/"
    F_out += out_name + ".F_out.txt"
    combined_out = paths.SCANNER_OUTPUT_PATH + "/"
    combined_out += out_name + ".dual_out.txt"

    is_archive = tarfile.is_tarfile(sys.argv[1]) or zipfile.is_zipfile(
        sys.argv[1])
    parse_output(sys.argv[1], is_archive, F_out, N_out)
    #subprocess.call(["rm", F_out])
    #subprocess.call(["rm", N_out])
    #print(str(parse_combined_file(combined_out)))
    scan_list = parse_combined_file(combined_out)
    clean() #get rid of the internal files since we no longer need them
    if not scan_list:
        raise Exception(
            "Failed to parse FOSSology and Ninka scanner output.")
    else:
        print(generate_json(scan_list))
