#!/usr/bin/python
"""
Output results of FOSSology and/or Ninka scans of a file or multiple files.
"""

import json

class FNOutputs:
    """
    Store and output results of FOSSology and/or Ninka scans of a file or
    multiple files.
    
    This class handles both single file scans and packages with multiple files.
    """
    
    results = {
        "package_name": "NONE",
        "file_results": {}
    }
    """
    Package name and file scan results.
    package_name should be set other than "NONE" if more than one file is
    present, but may be set for only one file if it belongs to a package.
    """
    
    def __init__(self, package_name):
        self.results["package_name"] = package_name
    
    def add_file_results(self, file_name, foss_output, ninka_output):
        """
        Adds the results of a single file scan to the package object.
        
        For now, this function assumes that both scanners were run and returned
        some output, and each scanner only returned one license.
        """
        
        if foss_output == ninka_output:
            concluded = foss_output
            comments = "#fossology #ninka"
        else:
            concluded = "NOASSERTION"
            comments = "#fossology:" + foss_output + " #ninka:" + ninka_output
        
        self.results["file_results"][file_name] = {
            "licenseConcluded": concluded,
            "licenseComments": comments
        }
    
    def get_json(self):
        """
        Outputs the result object as JSON.
        
        Example:
        '{"package_name": "superheroes", "file_results": {"spiderman": {"licenseComments": "#fossology:Spiderman #ninka:Spidey", "licenseConcluded": "NOASSERTION"}, "batman": {"licenseComments": "#fossology #ninka", "licenseConcluded": "Batman"}}}'
        """
        
        return json.dumps(self.results)
