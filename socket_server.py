import socket

def server():
    host = socket.gethostbyname(socket.gethostname())
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    conn, address = server_socket.accept()
    print(conn)
    print("Connection from: ", address)
    print(conn)

    while True:
        data = conn.recv(4096).decode()
        print("User: " + str(data))
        
        message = input("->")
        conn.send(message.encode())
            
    
    server_socket.close()    

server()
