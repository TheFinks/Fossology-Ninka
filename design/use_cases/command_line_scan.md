License determiner performs local FOSSology-Ninka scan through command line
===========================================================================
1.	**Title:** License determiner performs local FOSSology-Ninka scan through command line
2.	**Primary Actor:** User tasked with determining artifact licenses
3.	**Goal in Context:** To speed the determination of artifact licenses by comparing the output of multiple automatic license scanners
4.	**Stakeholders and Interests:**
    1.	**License determiners:**
        1.	To determine and communicate artifact licenses
        2.	To automate and quicken the license determination process
    2.	**Artifact consumers:**
        1.	To receive accurate and clear artifact licensing information
        2.	To be able to comply easily with artifact licenses
5.	**Preconditions:**
    1.	Artifacts contain some licensing information (e.g., in comments)
    2.	FOSSology and/or Ninka accurately assert licensing information
    3.	The license determiner has the knowledge, experience, and resources to manually resolve conflicting license scanner assertions
6.	**Main Success Scenario:** Output allows the license determiner to accurately and completely determine artifact licenses
    1.	A provisional SPDX document is output to the local file system
    2.	SPDX fields on which FOSSology and Ninka agree are filled out
    3.	SPDX fields on which FOSSology and Ninka conflict are marked NO ASSERTION
    4.	A data structure within the SPDX Comments field identifies conflict fields and lists the conflicting assertions
7.	**Failed End Conditions:**
    1.	Failure to run FOSSology or Ninka on a local package, or
    2.	Failure to compare FOSSology and Ninka output, or
    3.	Failure to create a provisional SPDX document on the local file system
8.	**Triggers:**
    1.	User is tasked with determining licenses for artifacts belonging to the user’s organization
    2.	User is tasked with determining licenses for third-party artifacts that the user’s organization would like to use
    3.	Manual or automated command-line execution of FOSSology-Ninka
9.	**Notes:** FOSSology-Ninka itself does not guarantee accurate and complete determination of artifact licenses. Artifacts may lack (complete) licensing information; FOSSology or Ninka determinations may be inaccurate; the license determiner may be unable to manually resolve conflicting license scanner assertions. FOSSology-Ninka aims to quicken the license determination process over purely manual review.
10.	**Example:** A user is tasked with determining the licenses used in a third-party software package. The user provides the local path to the package as an argument to FOSSology-Ninka. FOSSology-Ninka calls FOSSology and Ninka serially on the package, compares their assertions, and outputs a provisional SPDX document. The document records that both scanners assert that the license is GPLv3. The user may use some other tool to create a final SPDX document indicating human review.
