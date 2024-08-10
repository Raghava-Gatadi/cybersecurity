## [Project : AES Encryption and Decryption in Socket Programming](Cryptography)

### Overview

This project establishes a secure connection between a client and a server (MacBook and Windows) using socket programming. The messages exchanged between the client and server are encrypted using the AES (Advanced Encryption Standard) algorithm. The AES function implemented in the code is capable of utilizing 128-, 192-, and 256-bit keys for encryption and decryption.

### Key Features

- **Dynamic Key Management:** Instead of using a fixed key for every session, the code allows users to include a key in their messages. The key is added using the delimiter `\~`. If multiple delimiters are found in the message, the last one is used as the key. If no delimiter is found, the previous key is used.

### Instructions

1. Clone the folder in to your desktop.
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
