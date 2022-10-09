import socket
sockfd = socket.socket()
host = socket.gethostname()
port = 3518
sockfd.connect((host,port))
string = str(input("Enter the String: "))
sockfd.send(string.encode())
print(sockfd.recv(1024).decode())
sockfd.close()
