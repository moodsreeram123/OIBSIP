import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

clients = []
names = []
clients_lock = threading.Lock()


def broadcast(message):
    with clients_lock:
        recipients = clients.copy()
    for client in recipients:
        try:
            client.sendall(message)
        except OSError:
            remove_client(client)


def remove_client(client):
    with clients_lock:
        if client not in clients:
            return
        index = clients.index(client)
        clients.pop(index)
        name = names.pop(index)

        try:
            client.close()
        except OSError:
            pass

        broadcast(f"{name} left the chat.".encode())


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except (OSError, UnicodeDecodeError):
            break

    remove_client(client)


def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"Connected: {address}")

        try:
            client.sendall(b"NAME")
            name = client.recv(1024).decode().strip()
            if not name:
                client.close()
                continue
        except (OSError, UnicodeDecodeError):
            client.close()
            continue

        with clients_lock:
            names.append(name)
            clients.append(client)

        print(f"{name} joined the chat.")
        broadcast(f"{name} joined the chat!".encode())

        client.sendall("Connected to the chat!".encode())

        thread = threading.Thread(target=handle_client, args=(client,), daemon=True)
        thread.start()


if __name__ == "__main__":
    receive_connections()