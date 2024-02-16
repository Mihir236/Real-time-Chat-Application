import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received from {client_address}: {message}")  # Print the received message
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except ConnectionResetError:
            remove_client(client_socket)
            break


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)
    print("[SERVER] Server is listening on port 5555...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

clients = []

start_server()