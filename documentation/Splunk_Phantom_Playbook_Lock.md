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

5. Next we will log into **Splunk>Phantom** and manually sync the playbooks via Source Control. Go to `Playbooks` from the home dropdown menu, click the `update from source control` green button on the right-hand side. Select the correct **"Source Control"** from the dropdown menu, select `Force Update` and click the green **"Update"** button.

![Source Sync](https://i.imgur.com/2Qi3p05.jpg)

6. Now we will want to unzip the downloaded repository from step 3. We will need to get the `SHA1` hash from the Playbook `.py` file and make a note of it. Make sure you get the `SHA1` in all lowercase alphanumeric format. We will use **"Hash Tab"** to calculate our `SHA1`.

![File Hash](https://i.imgur.com/FK2D9SV.jpg)

7. We will edit the playbook `.json` file to include the `SHA1` file hash of the `.py` playbook file. Make sure you save the changes to the `.json` file before uploading back to GitHub.

![JSON](https://i.imgur.com/1dFZmr4.jpg)

8. Now we will upload the `.py` and `.json` files back to GitHub.

![FileUpload](https://i.imgur.com/ANkXJqc.jpg)

9. Next we will log back into **Splunk>Phantom** and manually sync the playbooks via Source Control. Go to `Playbooks` from the home dropdown menu, click the `update from source control` green button on the right-hand side. Select the correct **"Source Control"** from the dropdown menu, select `Force Update` and click the green **"Update"** button.

![Source Sync](https://i.imgur.com/2Qi3p05.jpg)

10. Now the playbook should be updated without the visual editor being locked.
