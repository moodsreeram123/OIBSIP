import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

def receive_messages(client, name):
    try:
        while True:
            message = client.recv(1024)
            if not message:
                break
            decoded = message.decode()
            if decoded == "NAME":
                client.sendall(name.encode())
            else:
                print(decoded)
    except (OSError, UnicodeDecodeError):
        pass
    finally:
        print("Disconnected from server.")
        try:
            client.close()
        except OSError:
            pass


def send_messages(client, name):
    try:
        while True:
            message = input()
            if message.lower() == "/quit":
                break
            client.sendall(f"{name}: {message}".encode())
    except (EOFError, OSError):
        pass
    finally:
        client.close()


def main():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except OSError as error:
        print(f"Could not connect to server: {error}")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client, name), daemon=True)
    receive_thread.start()

    send_messages(client, name)


if __name__ == "__main__":
    main()