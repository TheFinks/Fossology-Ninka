Fossology-Ninka 1.0
===================

Overview
--------

The purpose of this project is to develop a tool to generate SPDX documents that combine the outputs of [FOSSology] (http://www.fossology.org/projects/fossology) and [Ninka] (http://ninka.turingmachine.org/). A software file or package will be passed to each scanner in sequence. The output will be commpared and combined into one SPDX document. The result will give end users the licensing information that they need to determine how the scanned software may be used. Combining the two outputs leverages the strengths of each scanning engine.

This project may be integrated with other tools in the SPDX ecosystem. In particular, FOSSology-Ninka may be called as part of the do_spdx() SPDX document generation process being developed for [Yocto](https://www.yoctoproject.org/) builds.

### Future Goals
* Generation of complete SPDX documents, including manual conflict resolution between FOSSology and Ninka results
* Integration with third-party SPDX databases and web viewers/editors
* Attempt to optimize FOSSology execution time

Copyright
---------
Code and documentation are jointly copyrighted by:
* Doug Richardson
* [James Thompson] (https://github.com/jthomp24)
* [Jon von Kampen] (https://github.com/jvonkampen0)

See also our code and documentation [licenses](https://github.com/TheFinks/Fossology-Ninka/blob/master/LICENSE.md).

System Requirements
-------------------
In general, your system should meet [FOSSology's performance recommendations](http://www.fossology.org/projects/fossology/wiki/SysConfig), which depend on the maximum file or package size you intend to scan.

The FOSSology-Ninka dual scanner is developed and tested on Ubuntu 12.04 LTR with the latest version of Python 2.

Installation
------------
1. Install and configure [FOSSology] (http://www.fossology.org/projects/fossology/wiki/Ubuntu_Install_2_5) and [Ninka] (http://ninka.turingmachine.org/#sec-3) and their prerequisites as needed. Please refer to their respective documentation for instructions on how to do so.
2. Install Python 2, e.g., by executing `sudo apt-get install python2.7` on a Debian-like Linux distribution.
3. Download the files from the src folder. All of these files MUST be in the same folder to work. Apart from that there are no restrictions on where to place the software save for what your system has imposed.
4. Open paths.py with whatever editor you prefer. Change FOSSOLOGY_AGENT_PATH to the location of Nomos (the FOSSology license scanning agent). If you do not know, go to the command prompt and type `find / -name nomos`. Depending on your system, you may need root privileges (or `sudo`) to do so. If multiple FOSSology instances come up, choose whichever one you want. Do NOT include the name "nomos" in your path (that's handled by a separate variable). For example, if you choose to use `/usr/lib/fossology/agents/nomos`, you would enter `/usr/lib/fossology/agents/`. Do the same thing with the directory for "ninka.pl" for the variable NINKA_PATH.
5. If all our files are present and the Nomos and Ninka paths are correct, then you are ready to use the software.  Happy scanning.

Usage
-----
`./dual_scan.py file_or_archive options`

**Example:** `./dual_scan.py archive.tar.bz2 -v`

After that the process is entirely automated.  The results will be printed out as a JSON string.

**Options:**
-v activates the verbose mode.  This prints out messages indicating the progress of the process.

**Warning:** The scanning portion of the process can take a long time.

Intended Audiences
------------------
* [FOSSology] (http://www.fossology.org/projects/fossology) developers and users
* [Ninka] (http://ninka.turingmachine.org/) developers and users
* [Software Package Data Exchange (SPDX)] (http://spdx.org/) document authors
* [Yocto] (https://www.yoctoproject.org/) builders
* Additional SPDX ecosystem tools developed by fellow students in CSCI 4900/Internet Systems Development (spring 2014) at the [University of Nebraska at Omaha](http://www.unomaha.edu)

Contributions, Bug Tracking, and Code Management
------------------------------------------------
We welcome all pull requests! Some requests may be declined with the option to resubmit with certain specified changes. You are also invited to open up an issue to report a bug, request a new feature, or offer advice.

All technical decisions (including whether to accept a pull request) will be made by the unanimous consent of the named core contributors (see below). Additional core contributors will be designated by unanimous consensus of the existing core contributors. Core contributors may also abstain from voting on any decision. This decision mechanism may be revised in the future if it becomes unwieldy.

Following the spring 2014 semester, project administration will be wholly transferred to [Matt Germonprez](http://myweb.unomaha.edu/~mgermonprez/vita.html) and the [University of Nebraska at Omaha](http://www.unomaha.edu) ("transferees"). The founding contributors’ code and other artifacts will be licensed to the transferees for unlimited reuse, modification, and relicensing. The transferees will receive all core contributor decision-making powers.

System Design
-------------
Please refer to our [design folder](https://github.com/TheFinks/Fossology-Ninka/tree/master/design):
* [Architecture/data flow diagram](https://github.com/TheFinks/Fossology-Ninka/blob/master/design/DFD.jpg)
* [Use cases](https://github.com/TheFinks/Fossology-Ninka/blob/master/design/Use%20Cases.docx)
* [User interface mockups](https://github.com/TheFinks/Fossology-Ninka/tree/master/design/ui_mockups)
* [Code mockups](https://github.com/TheFinks/Fossology-Ninka/tree/master/design/code_mockups)

Some older project documentation is located in [README_old](https://github.com/TheFinks/Fossology-Ninka/tree/master/README_old) until it's updated and probably converted to Markdown.

Core Contributors
-----------------
* Doug Richardson
* [James Thompson] (https://github.com/jthomp24)
* [Jon von Kampen] (https://github.com/jvonkampen0)

overseen by [Matt Germonprez](http://myweb.unomaha.edu/~mgermonprez/vita.html) for CSCI 4900/Internet Systems Development (spring 2014) at the [University of Nebraska at Omaha](http://www.unomaha.edu).
