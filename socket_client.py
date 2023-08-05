import socket

def client():
    host = socket.gethostbyname(socket.gethostname())
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        message = input("->")
        client_socket.send(message.encode())

        data = client_socket.recv(4096).decode()
        print("Server: " + data)

        if message == "bye":
            client_socket.close()

    client_socket.close()

client()

