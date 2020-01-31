# Splunk>Phantom Playbook Lock
Many of us that work with **Splunk>Phantom** know that if you change the 
Python Source code outside a custom script block, the entire visual editor will now be locked forever. 
The following how-to will show you how to edit the python source code and prevent the visual editor from going into a lock state.

1. The first step in preventing **Splunk>Phantom** from locking is to use **GitHub** as Source Control within the Phantom platform

2. Once SourceControl is configured with GitHub, we will want to make any source code changes to the Python code from the GitHub editor.
![Edit SourceCode](https://i.imgur.com/F2o6dfl.jpg)


3. Now that all source code changes have been compleated, we will want to download the entire repository from GitHub via `.zip`

![Download SourceCode](https://i.imgur.com/vO3pHOW.png)

4. Once the repository has been downloaded from GitHub and saved on your local machine we will want to delete the playbook we made changes too. Delete the playbook `.py` file from the repository.

![Delete Python](https://i.imgur.com/fm0kkuR.jpg)

5. Next we will log into Splunk>Phantom and manually sync the playbooks via Source Control. Go to `Playbooks` from the home dropdown menu, click the `update from source control` green button on the right-hand side. Select the correct "Source Control" from the dropdown menu, select `Force Update` and click the green "Update" button.

![Source Sync](https://i.imgur.com/2Qi3p05.jpg)
