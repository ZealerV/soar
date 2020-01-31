# Splunk>Phantom Playbook Lock
Many of us that work with **Splunk>Phantom** know that if you change the 
Python Source code outside a custom script block, the entire visual editor will now be locked forever. 
The following how-to will show you how to edit the python source code and prevent the visual editor from going into a lock state.

1. The first step in preventing **Splunk>Phantom** from locking is to use **GitHub** as Source Control within the Phantom platform

2. Once SourceControl is configured with GitHub, we will want to make any source code changes to the Python code from the GitHub editor.
![Edit SourceCode](https://i.imgur.com/F2o6dfl.jpg)


3. Now that all source code changes have been compleated, we will want to download the entire repository from GitHub via `.zip`

![DownloadSourceCode](https://i.imgur.com/vO3pHOW.png)

4. 
