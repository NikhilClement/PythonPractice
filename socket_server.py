import socket
server_socket = socket.socket()
print "Socket successfully created"
port = 11111
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Empty string is passed for server to accept
#connections all available IPv4 interfaces
server_socket.bind(('', port))
print "socket bound to %s" %(port)
#set a limit on the backlog of pending connections in the queue
server_socket.listen(5)
print "listening"
while True:
    #block and wait for incoming connection
    client, addr = server_socket.accept()
    print 'Got connection from\n', addr
    #save the string whose occurrence is to be counted
    string_to_be_searched = client.recv(1024)
    #open the file
    f = open("file.txt", "r")
    #read the entire file and count the occurrence
    #readline() must be used to read individual lines
    #within a loop, if the file is large
    count = f.read().count(string_to_be_searched)
    f.close()
    client.send(str(count))
    client.close()
