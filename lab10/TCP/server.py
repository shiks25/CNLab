import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Server ------------------') 

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind((serverName, serverPort ))

serverSocket.listen(3)

while True:
    print("Server waiting for connection...")
    clientSocket, addr = serverSocket.accept()
    print("Client connected from",addr)
    while True:
        data = clientSocket.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        print("Received from client: %s"%data.decode("utf-8"))
        try:
            clientSocket.send(bytes('Hi client,Data recieved by server', 'utf-8'))
            
        except:
            print("Client Exited.")
    clientSocket.close()
