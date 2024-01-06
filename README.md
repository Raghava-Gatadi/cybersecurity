# Repository: SecureSocketAndScanner

This repository contains two projects focusing on network security and communication. The projects are independent, each serving a unique purpose.

## [Project 1: AES Encryption and Decryption in Socket Programming](Cryptography)

### Overview

This project establishes a secure connection between a client and a server (MacBook and Windows) using socket programming. The messages exchanged between the client and server are encrypted using the AES (Advanced Encryption Standard) algorithm. The AES function implemented in the code is capable of utilizing 128-, 192-, and 256-bit keys for encryption and decryption.

### Key Features

- **Dynamic Key Management:** Instead of using a fixed key for every session, the code allows users to include a key in their messages. The key is added using the delimiter `\~`. If multiple delimiters are found in the message, the last one is used as the key. If no delimiter is found, the previous key is used.

### Instructions

1. Clone the repository.
2. Compile and run the server code on one machine.
3. Compile and run the client code on another machine.
4. Communicate securely with encrypted messages.

### Example

```python
# Example Message
message = "Hello, World!\~my_secret_key"

# Encrypted Message Sent Over the Network
# ...

# Decryption at the Receiver's End
# ...
```


# [Project 2: Network Scanner](Network_Scanner)

## Overview

This Django project provides a web-based network scanning tool that identifies systems connected to the user's network. Utilizing the Django framework, the application displays the IP addresses and MAC addresses of the connected systems and identifies any open ports on those systems. The project leverages the power of Django's web framework for a user-friendly and interactive experience.

## Instructions

1. Clone the repository.
2. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```
3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```
4. Open your web browser and navigate to `http://localhost:8000` to access the network scanner application.

5. Use the web interface to scan the network and view the list of connected systems, their IP addresses, MAC addresses, and open ports.

## Example

Visit `http://localhost:8000` in your web browser after running the development server to start using the network scanner.

Feel free to explore and utilize this Django-based network scanner for understanding the devices connected to your network and identifying open ports. If you encounter any issues or have suggestions, please open an issue in the repository. Happy scanning!
