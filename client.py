import socket
import threading  # Import threading module

def send_message(client_socket):
    while True:
        message = input("Enter message to send: ")
        client_socket.send(message.encode("utf-8"))

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        print("Received message:", message)

def main():
    server_ip = "127.0.0.1"  # Server IP address
    server_port = 5555  # Server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Start sending messages in a separate thread
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

    # Receive messages in the main thread
    receive_messages(client_socket)

    # Close the socket when done
    client_socket.close()

if __name__ == "__main__":
    main()
