#!/usr/bin/python

"""
This method is a plugin for custom methods meant to interact with the do_spdx
project.

(so far only one function is here, but I am keeping this space separate incase
the do_spdx project wants to further customize the scanner while keeping the
functions of the main scanner relatively autonomous)

@author Doug Richardson
@author Jon von Kampen
@author James Thompson

@license Apache License 2.0
"""

def make_json(scan_list):
    """
    Creates a JSON object custom-designed for the do_spdx project.
    The input for this method is a tuple with 5 parts.
    The tuple contains the name of the scanned package, the name of the
    scanned fike, the SHA-1 checksum, the license declared (assuming both
    scanners agree), and the comments section.

    The format is as follows: (package_name, file_name, checksum,
    license_concluded, comments)

    This method was created because do_spdx requires a very specific format.
    This format does not allow for package names or comments.  However, those
    fields are imported incase future do_spdx spec changes to allow for this.

    Because of time constraints and the JSON generator being...uncooperative
    This will generate the object manually.
    """

    results = False

    for scan in scan_list:
        #package_name = scan[0] #not used here
        file_name = scan[1]
        checksum = scan[2]
        concluded = scan[3] #This is license declared
        #comments = scan[4] #not used (although it really should be)

        result = "{\"file_level_info\":["
        result += "{\"FileName\":\"" + file_name + "\","
        result += "\"FileType\":\"SOURCE\","
        result += "\"FileChecksum\":\"" + checksum + "\","
        result += "\"FileChecksumAlgorithm\":\"SHA1\","
        result += "\"LicenseConcluded\":\"NOASSERTION\","
        result += "\"LicenseInfoInFile\":\"NOASSERTION\","
        result += "\"FileCopyrightText\":\"NOASSERTION<Vtext>\"},],"

        result += "\"extracted_license_info\":["
        result += "{\"LicenseName\":\"" + concluded + "\","
        result += "\"ExtractedText\":\"NOASSERTION<Vtext>\","
        result += "\"LicenseCrossReference\":\"NOASSERTION\"},]}"

        #Using a list to make the output easier to customize later if needed
        if not results:
            results = [result]
        else:
            results.append(result)

        #This "emulates" a JSON dump
        output = ""
        for item in results:
            output += item

    return output
