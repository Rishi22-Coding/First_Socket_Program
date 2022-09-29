import socket

ServerSocket = socket.socket()
print("Socket Created")

ServerSocket.bind(("localhost", 9999))
ServerSocket.listen(3)
print("Waiting for the Connections")

while True:
    ClientSocket, address = ServerSocket.accept()
    ClientName = ClientSocket.recv(1024).decode()
    print("Connected with ", address, ClientName)

    ClientSocket.send(bytes("Conn Established", "utf-8"))
    ClientSocket.close()
