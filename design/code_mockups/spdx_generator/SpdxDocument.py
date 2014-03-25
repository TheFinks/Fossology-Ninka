#This document is created by Doug Richardson
#This document is licesned under GPLv2 or any newer version

#This is a SPDX-Document skeleton library to use for later
#This is strictly a library (it doesn't have any methods within it...
#...only members)

#Default variables will be removed once a writer is made
#EXCEPT spdx_version (this is always for the 1.2 spec)

#any field with an asterix (*) after it is required for the SPDX-spec

#SPDX docment information
#(I didn't think sub-classing these were necessary)

spdx_version = "SPDX-1.2" #the SPDX spec used, DEFAULT WILL BE KEPT*
data_license = "GPL-2.0+" #the licesnse used*
document_comment = "This is a demo SPDX document" #document comments

Spdx_Document = [spdx_version, data_license, document_comment]
Spdx_Document_Members = ["spdxVersion", "dataLicense", "documentComment"]

#Creator Information

creator = "Tool: Fossology-Ninka" #person or tool used to create*
created = "2014-02-25T 20:07:30Z" #when it was created*
	#created is in YYYY-MM-DDT HH:MM:SSZ format...
	#...with leading zeros if need be
creator_comment = "" #comments from the creator
license_list_version = "LicesnseListVersion 1.19" 
	#version of the SPDX license list used

Creator_Information = [creator, created, creator_comment, license_list_version]
Creator_Information_Members = [
	"creator", "created", "creatorComment", "licesnseListVersion"]


#Package Information


package_name = "DEFAULT PACKAGE" #the name of the package checked*
package_version = "" #the version of the package checked
package_file_name = "" #the full file name of the package checked
	#for example, ninka-1.1.tar.bz2 would be the file name for ninka
package_supplier = "NOASSERTION" #where the package came from
package_originator = "NOASSERTION" #who created the package
package_download_location = "NOASSERTION" 
	#where the package was downloaded from*
package_verification_code = "0da55481fef187198cce91574bde684"
	#A amalgated SHA1 checksum of each of the files in the package*
	#...independently and combined with one another
package_checksum = ""
	#A SHA1 checksum on the package as a holistic entity
package_home_page = "NOASSERTION"
	#The home page the package came from
source_information = "" #Any other relevant background info
package_concluded_license = "NOASSERTION"
	#The concluded license of the package
	#If the package contains several licenses, AND or OR fields are used
all_license_information_from_files = "NOASSERTION"
	#This is EACH license from the files (no duplicates)*
package_declared_license = "NOASSERTION"
	#This is what licesnse the package creators declared"
package_license_comments = ""
	#This is the comments on the licenses
package_copyright_text = "NOASSERTION"
package_summary_description = "" #a short description about the package
package_detailed_description = "" #a detailed description of the package

Package_Information = [
	package_name, package_version, package_file_name, package_supplier, 
	package_originator, package_download_location, 
	package_verification_code, package_checksum, 
	package_home_page, source_information, 
	package_concluded_license, all_license_information_from_files, 
	package_declared_license, package_license_comments, 
	package_copyright_text, package_summary_description, 
	package_detailed_description
	]

Package_Information_Members = [
	"PackageName", "PackageVersion", "PackageFileName", 
	"PackageSupplier", "PackageOriginator", "PackageDownloadLocation", 
	"PackageVerificationCode", "PackageChecksum", "PackageHomePage", 
	"PackageSourceInfo", "PackageLicenseConcluded", 
	"PackageLicenseInfoFromFiles", "PackageLicenseDeclared",
	"PackageLicenseComments", "PackageCopyrightText", 
	"PackageSummary", "PackageDetailedDescription"
	]
#again, sorry about the formatting

#Other Licensing Info Detected
#One instance for any non SPDX-Recognized license

identifier_assigned = "" #This is done if the license is not on the SPDX-list
extracted_text = "" #This is the extracted text from the "ref-ed" license
license_name = "" #This is the name of the extracted license
license_cross_reference = "" #this points to the official info...
	#...for the extracted license
license_comment = "" #This is a comment on the extracted license

Other_Licensing_Info = [
	identifier_assigned, extracted_text, license_name, 
	license_cross_reference, license_comment
	]

Other_Licensing_Info_Members = [
	"LicenseID", "ExtractedText", "LicenseName", 
	"LicenseCrossReference", "LicenseComment", "LicenseCrossReference", 
	"LicenseComment"
	]

#File Information
#this is required for each file within a given package

file_name = "ninka.pl" #the name of the file*
file_type = "SOURCE" #the type of file*
	#options include SOURCE, BINARY, ARCHIE, or OTHER
file_checksum = "5745156dfed84" #the SHA-1 checksum of the file*
file_license_concluded = "NOASSERTION" #the HUMAN CONFIRMED license*
license_info_from_file = "LicenseRef-1" #the license info from the file
	#This is the 'license declared' part of the file*
file_license_comments = "(mockup doesn't have LicenseRef-Docs" 
	#comments on the license found
	#THIS is probably where we're going to put conflicts
file_copyright_text = "NOASSERTION" #The copyright information in a file*
artifact_of_project_name = "" #Indicates if the files was an artifact of...
	#...a speciic project
artifact_of_project_homepage = "" #Indicates the homepage of the parent project
artifact_project_URI = "" #indicates the URI of the parent project
file_comment = "" #indicates comments on the file proper
file_notice = "" #indicates potential legal notices for the file
file_contributor = "" #indicates the contributor of the file
file_dependencies = "" #indicates the dependencies of a given file

File_Information = [
	file_name, file_type, file_checksum, file_license_concluded,
	license_info_from_file, file_license_comments,
	file_copyright_text, artifact_of_project_name,
	artifact_of_project_homepage, artifact_project_URI,
	file_comment, file_notice, file_contributor, file_dependencies
	]
File_Information_Members = [
	"FileName", "FileType", "FileChecksum", "LicenseConcluded",
	"LicenseInfoInFile", "LicenseComments", "FileCopyrightText",
	"ArtifactOfProjectName", "ArtifactOfProjectHomepage",
	"ArtifactOfProjectURI", "FileComment", "FileNotice", "FileContributor",
	"FileDependency"
	]

#we will not be adding review information, as this scanner is pre-review
