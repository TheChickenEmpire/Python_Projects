import socket
while True:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname() 
    port = 9999 
    serversocket.bind((host, port)) 
    serversocket.listen(5) 
    clientsocket, addr = serversocket.accept()
    message = input()
    clientsocket.send(message.encode('ascii'))
    clientsocket.close() 