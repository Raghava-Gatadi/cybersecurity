# Repository: SecureSocketAndScanner

This repository contains two projects focusing on network security and communication. The projects are independent, each serving a unique purpose.

## Project 1: AES Encryption and Decryption in Socket Programming

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


# Project 2: Network Scanner

## Overview

This project provides a network scanning tool that identifies systems connected to the user's network. It displays the IP addresses and MAC addresses of the connected systems and identifies any open ports on those systems.

## Instructions

1. Clone the repository.
2. Compile and run the network scanner code.
3. View the list of connected systems, their IP addresses, MAC addresses, and open ports.

## Example

```bash
$ python network_scanner.py

Scanning the network...

IP Address       MAC Address        Open Ports
--------------   ----------------   ------------
192.168.1.1      00:1A:2B:3C:4D:5E   22, 80, 443
192.168.1.2      01:2A:3B:4C:5D:6E   80, 8080
# ...
```
