import socket
import threading
from AES import *
from colorama import Fore, Style

def receive_data(client_socket, block_size=16):
    data = b""
    while True:
        chunk = client_socket.recv(block_size)
        if not chunk:
            break
        data += chunk
        if len(chunk) < block_size:
            break
    return data

def send_data(client_socket, data):
    client_socket.sendall(data)

def handle_client(client_socket):
    while True:
        encrypted_data = receive_data(client_socket)
        reciever_1 = Style.BRIGHT + Fore.GREEN + "\nReceived Encrypted Data from client:" + Style.RESET_ALL
        reciever_2 = Style.BRIGHT + Fore.GREEN + "Decrypted text: " + Style.RESET_ALL
        print(reciever_1, encrypted_data)
        print(reciever_2, aes_decrypt(encrypted_data, 'SecretKey'))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    server_socket.bind(('0.0.0.0', port)) 
    server_socket.listen(1)

    print(f"Server listening on {port}...")

    client_socket, client_address = server_socket.accept()
    print('Connection from', client_address)

    # Start a new thread to handle receiving data from the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    while True:
        # Allow the server to send a message
        send = Style.BRIGHT + Fore.RED + "\nEnter your response: " + Style.RESET_ALL
        response = input(send)
        encrypted_response = aes_encrypt(response, 'SecretKey')
        data = Style.BRIGHT + Fore.RED + "Encrypted value of your Message: " + Style.RESET_ALL
        print(data, encrypted_response)
        send_data(client_socket, encrypted_response)

if __name__ == "__main__":
    main()
