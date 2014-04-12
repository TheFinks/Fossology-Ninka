#!/usr/bin/python

"""
Scan a file or archive with FOSSology and Ninka, then output a JSON string with
the file licenses, or the conflicting results from each scanner. Although
multiple files within a package may be scanned, output is a single unified
JSON. Output is intended for use in Software Package Data Exchange(R) 
SPDX(R))-compatible applications or documents.

@author Doug Richardson
@author Jon von Kampen
@author James Thompson

@license Apache License 2.0

@todo May want to add a "percentage completed" (in factors of 10) for the
archive scanner, as it can take a LONG time, and signs of progress would ease
the user experience.
@todo May want to add an initial check method to see if NOMOS and Ninka are
where files.py says they are (even if it's just checking if a file exists in
that location).
"""

import sys
import os
import subprocess
import tarfile
import zipfile
import json
import sys

import paths
from run_scanners import ninka_scan, foss_scan
from output_parser import ninka_parser, foss_parser, combined_parser

def get_file_from_absolute_path(path_name):
    """
    This trims down the absolute path so we can get the file name without
    extraneous directories.
    """
    path_list = path_name.split("/")
    return path_list[len(path_list) - 1]

def archive_scan(archive, scan_type, f_name):
    """
    Scans each file in an archive. This function take advantage of the fact
    that the tarfile and zipfile Python packages have identical method names.
    """
    if not f_name:
        sys.stderr.write("ERROR: Must specify an output file")
        archive.close()
        exit(1)
    else:
        f = open(f_name, 'w')
        for name in archive.getnames():
            path = paths.TEMP_ARCHIVE_UNPACK_PATH + "/" + name
            #Scan types can be n (Ninka) or f (FOSSology)
            if scan_type is 'n':
                f.write(str(ninka_scan(path)))
            elif scan_type is 'f':
                f.write(str(foss_scan(path)))

def clean():
    """
    Removes any temporary directories used by the scans.
    """
    if os.path.isdir(paths.TEMP_ARCHIVE_UNPACK_PATH):
        subprocess.call(["rm", "-r", paths.TEMP_ARCHIVE_UNPACK_PATH])
    if os.path.isdir(paths.SCANNER_OUTPUT_PATH):
        subprocess.call(["rm", "-r", paths.SCANNER_OUTPUT_PATH])

def check_file(file_name):
    """
    Currently, this deletes a file with an identical name and location to one
    that this method will need to write to.
    
    @todo An option to decide whether or not to overwrite (undecided)
    """
    if os.path.isfile(file_name):
        subprocess.call(["rm", file_name])

def run_scans(target, opts):

    verbose = False

    #Checks to see if any options are activated
    if opts:
        if opts == "-v":
            verbose = True

    """
    Runs both FOSSology and Ninka on a given file or package.
    """
    #print("Creating directories needed for the scanners to work")

    """
    Checks to see if the paths we need are there
    If they are not, it creates them

    (the archive path is meant for destruction, so it is assumed
    that it should not be there unless something went wrong)
    """

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

    if verbose:
        print("Checking file format")

    if tarfile.is_tarfile(target):
        if verbose:
            print(target + " identified as TAR file")
        archive = tarfile.open(target)
        if verbose:
            print("Extracting data")
        archive.extractall(paths.TEMP_ARCHIVE_UNPACK_PATH)
        if verbose:
            print("Starting Ninka scan")
        archive_scan(archive, 'n', ninka_out)
        if verbose:
            print("Ninka scan finished")
            print("Starting FOSSology scan")
        archive_scan(archive, 'f', foss_out)
        if verbose:
            print("FOSSology scan finished")
        archive.close()

    #This is the same as the tarfile method but with zipfile
    elif zipfile.is_zipfile(target):
        if verbose:
            print(target + " identified as ZIP file")
        archive = zipfile.open(target)
        if verbose:
            print("Extracting data")
        archive.extractall(paths.TEMP_ARCHIVE_UNPACK_PATH)
        if verbose:
            print("Starting Ninka scan")
        archive.scan(archive,'n', ninka_out)
        if verbose:
            print("Ninka scan finished")
            print("Starting FOSSology scan")
        archive.scan(archive,'f', foss_out)
        if verbose:
            print("FOSSology scan finished")
        archive.close()
    
    else: #assumes a single file
        if verbose:
            print("File is either not an archive or an unrecognized format;"
                " scanning as single file")
        path = paths.TEMP_ARCHIVE_UNPACK_PATH + "/" + target
        subprocess.call(["cp", target, paths.TEMP_ARCHIVE_UNPACK_PATH])
        #first with Ninka
        n_file = open(ninka_out, 'wb')
        if verbose:
            print("Starting Ninka scan")
        n_file.write(ninka_scan(path))
        if verbose:
            print("Ninka scan fnished")
        n_file.close()

        #next with FOSSology
        f_file = open(foss_out, 'w')
        if verbose:
            print("Starting FOSSology scan")
        f_file.write(foss_scan(path))
        if verbose:
            print("FOSSology scan finished")
        f_file.close()

    """
    NOTE: Due to Python limitations, this software currently can NOT scan any
    other archive types.
    """

def parse_output(target, is_archive, foss_file, ninka_file, opts):
    """
    Parses the FOSSology and Ninka scan output, and places the results in a
    unified file (for our internal use).
    
    The file format is archive_name;file_name;FOSSology_output;ninka_output
    """
    verbose = False

    if opts:
        if opts == "-v":
            verbose = True


    if not os.path.isfile(foss_file):
        sys.stderr.write("ERROR: " + foss_file + " not found")
        exit(1)
    elif not os.path.isfile(ninka_file):
        sys.stderr.write("ERROR: " + ninka_file + " not found")
        exit(1)
    else:
        out_name = get_file_from_absolute_path(target)
        if verbose:
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
        foss_lines = str(foss.read()).split("\n")
        ninka_lines = str(ninka.read()).split("\n")
        #If not equal, go with the shortest one, will put in later
        if len(foss_lines) == len(ninka_lines):
            for i in range(0, len(foss_lines) - 1):
                foss_out = foss_parser(foss_lines[i])
                ninka_out = ninka_parser(ninka_lines[i])
                if foss_out[0].strip() == ninka_out[0].strip():
                    output = archive_name + ";"
                    output += foss_out[0].strip() + ";"
                    output += foss_out[1] + ";"
                    output += ninka_out[1] + "\n"
                    output_file.write(output)

        foss.close()
        ninka.close()
        output_file.close()
        if verbose:
            print("Output file complete")

def parse_combined_file(file_name):
    """
    Parses the unified internal file that parse_output() created and places the
    results in a tuple that can be easily translated to a JSON object for use
    with SPDX 1.2.

    The input format is archive_name;file_name;FOSSology_output;ninka_output

    The output format is (archive_name, file_name, license_concluded, comments)
    """
    f = open(file_name, 'r')
    archive_name = "(ERROR)"
    file_name = "(ERROR)"
    license_concluded = "(ERROR)"
    comments = "(ERROR)"
    output = False

    for line in f:
        file_info = line.split(";")
        archive_name = file_info[0] #The name of the archive scanned
        file_name = file_info[1] #The name of the file scanned
        foss_out = file_info[2].split(",") #FOSSology's output
        ninka_out = file_info[3].split(",") #Ninka's output

        #If FOSSology and Ninka throw an error, skip this entry
        if foss_out[0] != "ERROR" and ninka_out[0] != "ERROR":
            result = combined_parser(foss_out, ninka_out)
            license_concluded = result[0]
            comments = result[1]
            if not output:
                temp = (archive_name, file_name,
                    license_concluded, comments)
                output = [temp]
            else:
                temp = (archive_name, file_name,
                    license_concluded, comments)
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
    print("USAGE: " + sys.argv[0] + " file_or_package")
    print("EXAMPLE: " + sys.argv[0] + " ninka.pl")

else:
    opts = False
    if len(sys.argv) == 3:
        opts = sys.argv[2]

    run_scans(sys.argv[1], opts)
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
    parse_output(sys.argv[1], is_archive, F_out, N_out, opts)
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
