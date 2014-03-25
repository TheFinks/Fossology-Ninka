#!/usr/bin/python
import SpdxDocument

print("{")
print("\t\"SpdxDocument\":\n\t{")
for index in range (len(SpdxDocument.Spdx_Document)):
	print("\t\t\"" + SpdxDocument.Spdx_Document_Members[index]
		+ "\": \"" + SpdxDocument.Spdx_Document[index] + "\",")

print("\t},\n\t\"CreatorInformation\":\n\t{")
for index in range (len(SpdxDocument.Creator_Information)):
	print("\t\t\"" + SpdxDocument.Creator_Information_Members[index]
		+ "\": \"" + SpdxDocument.Creator_Information[index] + "\",")

print("\t},\n\t\"FileInformation\":\n\t{")
for index in range (len(SpdxDocument.File_Information)):
	print("\t\t\"" + SpdxDocument.File_Information_Members[index]
		+ "\": \"" + SpdxDocument.File_Information[index] + "\",")

print("\t}\n}")
