import socket 
while True:
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = 'Python' 
        port = 9999
        clientsocket.connect((host, port)) 
        message = clientsocket.recv(1024) 
        clientsocket.close() 
        print (message.decode ('ascii')) 
    except:
        pass