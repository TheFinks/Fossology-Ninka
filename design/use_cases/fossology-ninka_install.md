System administrator installs FOSSology-Ninka
=============================================
1.	**Title:** System administrator installs FOSSology-Ninka
2.	**Primary Actor:** System administrator on behalf of users who determine artifact licenses
3.	**Goal in Context:** To speed the determination of artifact licenses by comparing the output of multiple automatic license scanners
4.	**Stakeholders and Interests:**
    1.	**System administrators:**
        1.	To provide users with the tools they need for their tasks
        2.	To ensure the availability and responsiveness of all user applications
    2.	**License determiners:**
        1.	To determine and communicate artifact licenses
        2.	To automate and quicken the license determination process
5.	**Preconditions:**
    1.	Installation of FOSSology and Ninka with appropriate system resources to run them serially
    2.	Installation of FOSSology-Ninka infrastructure components (e.g., Python interpreter)
6.	**Main Success Scenario:**
    1.	FOSSology-Ninka can successfully locate and execute FOSSology and Ninka
    2.	FOSSology-Ninka is executable by all authorized users
7.	**Failed End Conditions:**
    1.	System administrator cannot determine how to configure FOSSology-Ninka to access its dependencies (FOSSology, Ninka, Python, etc.)
    2.	FOSSology-Ninka is not executable by authorized users
8.	**Trigger:** License determiner requests installation
9.	**Notes:** This use case assumes that system administrators possess the requisite knowledge to install and configure FOSSology, Ninka, and Python for standalone operation (i.e., to function as expected in use cases other than FOSSology-Ninka).
