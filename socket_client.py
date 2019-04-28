import socket
s = socket.socket()
port = 11111
#server is on localhost
server_ip="127.0.0.1"
s.connect((server_ip, port))
s.send(raw_input("Enter the string to be counted for its occurrence\n"))
print s.recv(1024)
s.close()
