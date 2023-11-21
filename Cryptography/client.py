import socket
import threading
from AES import *
from colorama import Fore,Style

def receive_data(server_socket, block_size=16):
    data = b""
    while True:
        chunk = server_socket.recv(block_size)
        if not chunk:
            break
        data += chunk
        if len(chunk) < block_size:
            break
    return data

def send_data(server_socket, data):
    server_socket.sendall(data)

def handle_server(server_socket):
    while True:
        # Allow the client to send a message
        send = Style.BRIGHT + Fore.RED + "\nEnter your response: " + Style.RESET_ALL
        message = input(send)
        encrypted_message = aes_encrypt(message, 'testkey') 
        data = Style.BRIGHT + Fore.RED + "Encrypted value of your Message: " + Style.RESET_ALL
        send_data(server_socket, encrypted_message)
        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.0.0.144', 12345))

# Start a new thread to handle sending data to the server
server_thread = threading.Thread(target=handle_server, args=(client_socket,))
server_thread.start()

while True:
    encrypted_response = receive_data(client_socket)
    reciever_1 = Style.BRIGHT + Fore.GREEN + "\nReceived Encrypted Data from client:" + Style.RESET_ALL
    print(reciever_1, encrypted_response)
    reciever_2 = Style.BRIGHT + Fore.GREEN + "Decrypted text: " + Style.RESET_ALL
    print(reciever_2, aes_decrypt(encrypted_response, 'testkey'))

client_socket.close()

