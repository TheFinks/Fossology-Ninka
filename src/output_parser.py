#!/usr/bin/python

import license_compare

'''
    This software is written by Doug Richardson, with the help of
    Jon von Kampen and James Thompson.  It is licensed under
    the Apache License, version 2.0 (because it makes life easier for
    our sponsor, Matt)
'''


#default format is File myfile.c containes licence(s) L1, L2
def foss_parser(foss_in):
    foss_tokens = foss_in.split(" ")
    license = "F_ERROR" #If the file cannot be parsed
    file_name = "ERROR"
    
    #If it doesn't start with file, then nomos threw an error
    #The first license is on the 5th token

    if foss_tokens[0].strip() == 'File' and len(foss_tokens) > 4:
        for i in range(4, len(foss_tokens)):
            if license == "F_ERROR":
                license = foss_tokens[i]
            else:
                license += foss_tokens[i]
        file_name = foss_tokens[1]

    elif foss_tokens[0] == 'nomos:' and len (foss_tokens) > 2:
        temp = foss_tokens[2].split("/")
        file_name = temp[len(temp) - 1].replace("\"","")
        '''
            on non-files, nomos throws an error message
            in this message, the path is in quotes
        '''
        license = "ERROR"

    

    return (file_name, license)

#default format is file_name;license(s);[other stuff we don't need]
def ninka_parser(ninka_in):
    ninka_tokens = ninka_in.split(";")
    license = "F_ERROR"
    file_name = "ERROR"
    
    '''
        For our purposes we only need 2 things from ninkas output...
        ...the file name and the confirmed license.
        The other things in it are ignored.

        The file is the first token and the license(s) is/are...
        ...the second.

        The file is the absolute directory from the archive on downward.
        To compare it to fossology's output, we need to strip it...
        ...down to the file name only.
    '''

    if len(ninka_tokens) > 1:
        license = ninka_tokens[1]
        temp = ninka_tokens[0].split("/")
        file_name = temp[len(temp) - 1]

    return (file_name, license)


'''
    This assumes ninkas input, since it retains the file path from...
    ...the archive name on downward while nomos does not
'''
def file_path(ninka_in):
    output = "ERROR"
    tokens = ninka_in.split(";")
    if len (tokens) > 1:
        output = tokens[0]

    return output

#This method parses the final output
def combined_parser(foss_out, ninka_out):
    license_declared = "NOASSERTION"
    comments = ""

    final_out = False
    conflict = False  
    where_found = False

    '''
        -final_out accumulates matched licenses.
        -conflict records if there is a license conflict
        -where_found indicates whether a license is found in fossology
        ...ninka, or both.
    '''
    
    for foss_lic in foss_out:
        if conflict:
            break

        for ninka_lic in ninka_out:
            if conflict:
                break

            elif lic_compare(foss_lic, ninka_lic):
                if not final_out:
                    final_out = [lic_compare(foss_lic, ninka_lic)]
                else:
                    final_out.append(lic_compare(foss_lic, ninka_lic))
                break 
                #On to the next fossology license

            else:
                if ninka_lic == ninka_out[len(ninka_out) - 1]:
                    where_found = lic_found(
                        foss_lic, ninka_lic)

                    if where_found[0] and where_found[1]:
                        conflict = True
                        '''
                        A conflict occurs when
                        Both findings have licenses
                        (both where_found's are true)
                        but one is not in the other set
                        '''

    if not conflict:
        if not where_found or (where_found[0] and where_found[1]):
            license_declared = lic_join(final_out)
            comments = "#Fossology #Ninka"
            '''
            This is if both scanners have valid findings
            and no conflcits occur
            '''
        elif where_found[0] and not where_found[1]:
            if not final_out:
                final_out = [lic_compare(foss_lic, False)]
            else:
                final_out.append(lic_compare(foss_lic, False))
            license_declared = lic_join(final_out)
            comments = "#Fossology (names may not be SPDX standards compliant)"
            #This is if ONLY fossology has valid findings
        else:
            if not final_out:
                final_out = [lic_compare(False, ninka_lic)]
            else:
                final_out.append(lic_compare(False, ninka_lic))
            license_declared = lic_join(final_out)
            comments = "#Ninka (names may not be SPDX standards compliant)"
            #This is if ONLY ninka has valid findings
    else:
        '''
        On the event of a conflict, the license declared is
        NOASSERTION, and the comments state the license list

        (because of time constraints, this is the findings in
        verbatim from the scans, and not adjusted for SPDX-1.19)
        '''
        comments = "#Fossology "
        comments += lic_join(foss_out)
        comments += " #Ninka "
        comments += lic_join(ninka_out)
        comments += " (names taken directly from scanner results)"

    output = (license_declared.rstrip(), comments.rstrip())
    #I can't return the tuple directly or the compiler gets grumpy

    return output
        

#This compares the licenses with a comparison dictionary
def lic_compare(foss_out, ninka_out):
    match = False
    ninka_lic_found = ninka_out != "UNKNOWN"
    foss_lic_found = foss_out != "None"
    error_found = foss_out == "ERROR" and ninka_out == "ERROR"
    no_license = foss_out == "None" and ninka_out == "NONE"
    valid_search = ninka_lic_found and not error_found
    valid_search = valid_search and not no_license
    
    if(foss_out and ninka_out):
        if valid_search:
            for relation in license_compare.Licenses:
                if match:
                    break
                final = len(relation) - 1
                if foss_out == str(relation[0]):
                    if ninka_out.rstrip() == str(relation[1]):
                        match = relation[final]

        elif no_license:
            match = "NONE"

    elif(foss_out and not ninka_out):
        if foss_out != "None":
            for relation in license_compare.Licenses:
                if foss_out.strip() == str(relation[0]):
                    final = len(relation) - 1
                    match = relation[final]
                    break
            if not match:
                match = foss_out

    elif(ninka_out and not foss_out):
        if ninka_out != "UNKNOWN":
            for relation in license_compare.Licenses:
                if ninka_out.strip() == str(relation[1]):
                    final = len(relation) - 1
                    match = relation[final]
                    break
            if not match:
                match = ninka_out
    
    '''
        I know this method is a bit over-coupled (it tethers the
        SPDX-scanner and the dictionary lookup into one thing).
        However, it saves time cutting down the number of trips.
    '''

    return match

'''
    This method determines if a valid license is found
    (Error checking is handled outside, but I left that in to
    ...be thorough)
'''
def lic_found(foss_out, ninka_out):
    foss_found = False
    ninka_found = False
    no_license = foss_out == "None" and ninka_out.strip() == "NONE"
    no_foss = foss_out == "None" and not no_license

    if ninka_out.strip() != "UNKNOWN" and ninka_out.strip() != "ERROR":
        ninka_found = True
    if foss_found != "ERROR" and not no_foss:
        foss_found = True

    return (foss_found, ninka_found)
    

def lic_join(lic_list):
    result = "ERROR" #Shold never come up
    if len(lic_list) > 1:
        result = " AND ".join(lic_list)
    else:
        result = lic_list[0]
    return result
