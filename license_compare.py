#!/usr/bin/python

'''
This file is written by Doug Richardson.
This file is licensed under GPL2 or any newer version

The purpose of this file is to compare the licesnses found in...
...Ninka and Fossology, whom use different terminology.
(for example, GPLv2 is "GPL_v2" in fossology and "GPLv2" in Ninka)
This file will also contain the SPDX 1.19 definition when applicable

The format is as follows, (Fossology_output, Ninka_output, SPDX_name)
If any non-matching licesnses occur (for example, only Fossology reads...
...license-X), then any "blank spots" will be marked as False

Example: ("GPL_v2", "GPLv2", "GPL-2.0")
'''


'''
Notes for later

TODO: create a subroutine for the "seefile(name)" instances to refer back
...to it when doing the comparison OR just put "see file (name)" in the
proto SPDX comments as a proof of concept and build that later.

I don't think either scanner is specific in whether the BSD is
...new or "clause clear" in its type (although that doesn't matter, since
the output would conflict by semi-default).

Also, what do we do if SOME of the licesnes agree
assert those and put a conflict note about the rest?

I am assuming FOSsology's Free-SW is the free software license

NOTE: Ninka's none is not "NOASSERTION" (Fossology's might be)...
...That would be UNKNOWN.  However, since we can't confirm explicitness...
...we will treat it as such for now

I am assuming ninka made up "DoWhatTheFuckYouWantv2", so I am considering it
a non-licesne to be discarded

For special cases:
-If the output comes up ERROR in both cases, throw it out.
-If Ninka comes up UNKNOWN, then assume Fossology's confirmation only
--Do we do the same for FOSSOLOGY's None (it could mean none or unknown)?
'''

#Kept separate for now for sorting purpose
Non_Licenses = [
	("ERROR", "ERROR", False), ("None", "NONE", False),
	("UnclassifiedLicense", "UNKNOWN", False),
	(False, "DoWhatTheFuckYouWantv2", False)
	]

'''
	Fossology and Ninka are vague on some license output.  
	Because these are not explicit matches, we cannot confirm 
	their meaning.  However I put "approximations" and other 
	recorded instances here for future development.
'''

License_Approximations = [
	("BSD-style", "BSD3", False), ("BSD-style", "spdxBSD3", False), 
	("BSD-style", "spdxBSD4", False), ("BSD", "BSD3", False), 
	("BSD", "spdxBSD4", False), ("MIT-style", "MITX11", False),
	(False, "SameAsPerl", False),
	("Public-domain-claim", "publicDomain", False)
	(False, "DoWhatTheFuckYouWantv2", False)
	]

Licenses = [
	("GPL_v2", "GPLv2", "GPL-2.0"), ("GPL_v2+", "GPLv2+", "GPL-2.0+"),
	("Artistic", False, "Artistic-1.0"),
	("LGPL_v2.1+", "LesserGPLv2.1+", "LGPL-2.1+"),
	("RSA-Security", False, False), (False, "BeerWareVer42", False),
	("GPL", "GPLnoVersion", False), ("Free-SW", False, False),
	("Affero_v3+", "AGPLv3+", False), ("GPL_v3", "GPLv3", "GPL-3.0"), 
	("GPL_v3+", "GPLv3+", "GPL-3.0+")
	]
