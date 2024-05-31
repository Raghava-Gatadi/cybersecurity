# Repository: SecureSocketAndScanner

This repository contains multiple projects focusing on network security, communication and password management. The projects are independent, each serving a unique purpose.

## [Project 1: Password Strength Checker](Password_manager_checker/password_strength.py)
### overview
This project is a comprehensive Python application designed to evaluate password robustness. It employs a set of predefined criteria, including length, presence of uppercase and lowercase letters, numerical digits, and special characters, to determine the strength of a provided password. The goal of this project is to enhance security by encouraging the use of strong, complex passwords.

## [Project 2: Password Manager](Password_manager_checker/password_manager/)
### overview
This project is an efficient command-line password manager designed to enhance user security. It empowers users to generate, store, and retrieve passwords for various accounts. Key features include:

* **Command Line Interface:** A user-friendly and straightforward interface for seamless interaction.
* **Master Password Validation:** Ensures the authenticity of the user by validating the master password.
* **Password Management:** Allows users to create new entries, save them securely, and retrieve them when needed.
* **Clipboard Integration:** Automatically copies the retrieved password to the clipboard for easy use.
* **Random Password Generation:** Generates robust passwords composed of alphabets, numbers, and special characters, enhancing account security.
  
This project, while simple in its command-line approach, provides a robust solution for password management needs.


## [Project 3: AES Encryption and Decryption in Socket Programming](Cryptography)

### Overview

This project establishes a secure connection between a client and a server (MacBook and Windows) using socket programming. The messages exchanged between the client and server are encrypted using the AES (Advanced Encryption Standard) algorithm. The AES function implemented in the code is capable of utilizing 128-, 192-, and 256-bit keys for encryption and decryption.

## [Project 4: Network Scanner](Network_Scanner)

### Overview

This Django project provides a web-based network scanning tool that identifies systems connected to the user's network. Utilizing the Django framework, the application displays the IP addresses and MAC addresses of the connected systems and identifies any open ports on those systems. The project leverages the power of Django's web framework for a user-friendly and interactive experience.

## [Project 5: Real or Fake news detection](RealorFake_political_tweets.ipynb)

### Overview

This project was developed as a mini project during my 6th semester, focusing on detecting fake news using various machine learning models. The primary goal was to build a system capable of distinguishing between real and fake news articles with high accuracy.

### Key Features

- Data Preprocessing: Implemented various data preprocessing techniques such as tokenization, stemming, and removal of stopwords to clean and prepare the dataset for model training.
- Feature Extraction: Utilized different methods for feature extraction including TF-IDF, Word2Vec, and Word Embedding to convert text data into numerical representations.
- Model Training: Trained multiple machine learning models, including TF-IDF, BERT, Word2Vec, and Word Embedding, to identify patterns and features indicative of fake news.
- Performance Evaluation: Assessed the models using standard performance metrics such as Accuracy, Precision, Recall, and F1-score to ensure their effectiveness and reliability.


