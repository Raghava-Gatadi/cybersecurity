# Password Manager and Checker

This folder contains two projects related to password management and security.

## [Project 1: Password Strength Checker](password_strength.py)

This is a Python script that checks the strength of a password. It evaluates passwords based on length, use of special characters, numbers, and both lower and upper case letters.

### How to Use
1. Download the file
2. run the file using `Python3 password_strength.py`
3. Enter the input

## [Project 2: Command Line Password Manager](password_manager)

This is a command line application is used for managing passwords. It allows users to store, retrieve, and manage passwords securely.

### How to Use

1. Download the folder on your desktop
2. Firstly upgrade your pip version using `pip install --upgrade-pip`
3. Download the requirements using `pip install -r requirements.txt`
4. Go to the dbconfig.py file and update your workbench credentials
    ```python
    db = mysql.connector.connect(
      host ="YOUR_HOST",
      user ="YOUR_USER",
      passwd ="YOUR_PASSWORD"
    )
    ```
5. now run the config.py file, which is used to create, delete or recreate your database
   > python config.py [make/delete/remake]
6. not run the passwordmanager.py file:
   
   a. To add a entry to the database
   > python passwordManager.py add -s {sitename} -u {url} -e {email} -l {username}

   > Then your will be asked for masterPassword and the password for the website

   b. to rsearch for the entries
   * to retrieve all the entries
        > python passwordManager.py e

    * to search for the entries you can the switches -s to enter  sitename, -u for url, -e for email, -l for username Ex: 
        > python passwordManager.py e -s {sitename}
        > python passwordManager.py e -u {siteurl} -l {username}

    

