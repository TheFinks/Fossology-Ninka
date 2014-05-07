Output Format
=============

The primary gaol for this program is to determine what licenses were found and from which scanner they were found. 
The benefit of using such a program is to find hidden licenses by using two different scanners that specialize in 
finding different licenses. The most important seciont of our output will be the License Concluded and License 
Comments which will declare what licenses were found and by which scanner. 

The following example's depict how our program will represent the license's found and by which scanning tool. License
Concluded will display the license found only if both scanning tools found the same licenses. If each tool found a 
different license then the License Concluded section would be filled with "No Assertion", the same will happen if 
one tool finds a license and the other tool does not find a license. In the License Commens section the scanning 
tools will be dispayed following the # symbol and will be followed by a colon ":" which will be followed by the 
license that that scanning tool found or it will be followed by the words "none" if it did not find a license and the
other scanning tool did find something. There are two exceptions in which both licenses will be listed without 
anything following it, if both scanners find the same license/'s or if neither scanner finds a license.

o   Scenarios:

  -  1.

·         License Concluded: None

·         License Comments: #fossology #ninka

  -  2.

·         License Concluded: MIT

·         License Comments: #fossology #ninka

  -  3.

·         License Concluded: No Assertion

·         License Comments: #fossology:MIT #ninka:BSD-3

  -  4.

·         License Concluded: No Assertion

·         License Comments: #fossology:none #ninka:BSD-3

In order for our program to work with the current do_spdx group we had to make a few changes. What we did was (post 
scanning) take the package name, file name, licenses concluded, and comments (for conflicts and the like) and dump 
them into a usable JSON object.
Later we added a sha-1 checksum so external tools can verify that the file is genuine (assuming they use a sha-1 as 
a key to make sure).
do_spdx doesn't take all that data, but it's still passed to the method (since I am pretty sure later versions are 
going to want to have comments, since their needed object is pre-SPDX-1.2).

The following is what the end user should expect from our programin its current status

{
	"file_level_info":[
	{
		"FileName":"dual_scan.py",
		"FileType":"SOURCE",
		"FileChecksum":"12ff6dcb6e1a3cfeb95aabb83eaf25d29832dcde",
		"FileChecksumAlgorithm":"SHA1",
		"FileLicenseComments":"#FOSSology (names may not be SPDX standards compliant)",
		"LicenseConcluded":"Apache-2.0",
		"LicenseInfoInFile":"NOASSERTION",
		"FileCopyrightText":"NOASSERTION<Vtext>"
	},
	],
}
