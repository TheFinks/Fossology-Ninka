Fossology-Ninka
===============

Overview
--------

The purpose of this project is to develop a tool to generate SPDX documents that combine the outputs of [FOSSology] (http://www.fossology.org/projects/fossology) and [Ninka] (http://ninka.turingmachine.org/). A software file or package will be passed to each scanner in sequence. The output will be commpared and combined into one SPDX document. The result will give end users the licensing information that they need to determine how the scanned software may be used. Combining the two outputs leverages the strengths of each scanning engine.

FOSSology and Ninka are both scanning tools used to find licenses associated with a given software file or package. Each tool's algorithms can recognize particular licenses better than the other. The tool that we are creating intends to combine the output of both of these scanning tools into one cohesive document.  Refer to the documentation of FOSSology and Ninka for more information.

This project may be integrated with the projects of other CSCI 4900 groups. In particular, FOSSology-Ninka output may be stored in an SPDX database to be accessed by the SPDX Dashboard application. An enhancement to SPDX Dashboard may allow its use as an interface to manually resolve license declaration conflicts detected by FOSSology-Ninka.

In addition, we will develop a basic interface and spdx-finalizing procedure to enable end users to manually use our software as a stand-alone program.  These will consist of a simple uploader and SPDX finalizer.  The core scanner will be able to work independently of these sub-systems to allow for automation or future customization.
If we have completed the main tasks above, we will attempt to optimize FOSSology’s execution time to likewise increase the speed of our program. Also, if time permits, we will attempt to design a web based user interface.

Current Version
---------------
Version 1.0

License
-------
The source code will be covered under the [Apache 2.0] (https://github.com/TheFinks/Fossology-Ninka/edit/master/LICENSE.md)license declaration.
All documentation is licensed under Creative Commons CC-BY-SA

Copyright
---------

Technical Specifications
------------------------

System Design
-------------
The system design is represented by our [DFD Diagram] (https://github.com/TheFinks/Fossology-Ninka/edi/master/README.md).

Installation
------------

Usage
-----

Communities of Interest
-----------------------
Communication 
-------------
Code Management
---------------



To speed the determination of software artifact licenses by comparing the output of multiple automatic license scanners -- at this time, [FOSSology](http://www.fossology.org/projects/fossology) and [Ninka](http://ninka.turingmachine.org/).

Contributors
------------
* Doug Richardson
* James Thompson
* Jon von Kampen

overseen by [Matt Germonprez](http://myweb.unomaha.edu/~mgermonprez/vita.html) for CSCI 4900/Internet Systems Development (spring 2014) at the [University of Nebraska at Omaha](http://www.unomaha.edu).
