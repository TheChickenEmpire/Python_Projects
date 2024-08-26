import socket
from threading import Thread
from datetime import datetime
def Send(adr):
    print(1)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print(1)
    host = socket.gethostname() 
    print(1)
    port = 9999 
    print(1)
    serversocket.bind((host, port)) 
    print(1)
    serversocket.listen(5) 
    print(1)
    clientsocket, addr = serversocket.accept()
    print(1)
    message = input()
    print("\033[1A\033[K", end="")
    clientsocket.send(message.encode('ascii'))
    clientsocket.close() 
def Recieve(Name, Oc):
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = Oc 
        port = 9999
        clientsocket.connect((host, port)) 
        message = clientsocket.recv(1024) 
        clientsocket.close() 
        today = datetime.today()
        today = today.strftime("%d/%m")
        time = datetime.now()
        time = time.strftime('%h:%M ')
        now = time + today
        print(message.decode ('ascii')+' '+now) 
    except:
        pass
ar =input('Other Computer Name:\n')
t1 = Thread(target=Send)
t2 = Thread(target=Recieve)
while True:
    t1.start()
    t2.start()

    t2.join()
    thread_running = False