# Real-Time Chat Application

A beginner-friendly Python chat app that also includes the advanced features from the task: a tkinter desktop UI, multiple rooms, registration/login, SQLite message history, notifications, and emoji shortcodes.

## Run it

Open two or more terminals in this folder. The server and client are available as separate entry points:

```powershell
python server.py
```

Then, in each client terminal:

```powershell
python client.py
```

The original combined entry point is also supported:

```powershell
python chat_application.py server
python chat_application.py client
```

The default endpoint is `127.0.0.1:5050`. To use another endpoint, pass the same options to both processes:

```powershell
python server.py --host 0.0.0.0 --port 5051
python client.py --host 127.0.0.1 --port 5051
```

Register a username in the GUI, or log in with an existing account. Use **Join / create** to enter a room name. The `lobby` room is available automatically. Press Enter or click **Send** to chat.

## Features

- Threaded TCP server supports multiple simultaneous clients.
- Messages are bidirectional and include `[HH:MM] username:` timestamps.
- Disconnects and room joins are announced to room members.
- Passwords are stored as salted PBKDF2-SHA256 hashes, never as plaintext.
- The last 100 messages in a room load when a user joins it.
- The client rings the system bell when a message arrives while its window is unfocused.
- Common shortcodes such as `:smile:`, `:heart:`, `:thumbsup:`, `:wave:`, and `:laughing:` render as Unicode emoji.

## Storage and security transparency

The server creates `chat_history.db` beside the script. SQLite stores registered usernames and salted password hashes in `users`, and room messages with room name, username, text, and timestamp in `messages`. The database is local to the server process and is not deleted automatically.

Messages are **not end-to-end encrypted**. They are sent as readable JSON over a plain TCP connection and are stored as readable text in SQLite. This implementation is intended for local learning and trusted networks; it does not provide TLS, production session management, moderation, rate limiting, or account recovery.

## References

- Python socket documentation: https://docs.python.org/3/library/socket.html
- Python threading documentation: https://docs.python.org/3/library/threading.html
- Python sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html

The socket design follows the standard listening socket, accepted client socket, `recv`, and `sendall` connection pattern described in the official Python documentation.
