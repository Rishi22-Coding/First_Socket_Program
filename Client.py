import socket
ClientSocket = socket.socket()
ClientSocket.connect(("localhost", 9999))

ClientName = input("Enter Client Name")
ClientSocket.send(bytes(ClientName, "utf-8"))

result = ClientSocket.recv(1024).decode()
print(result)
