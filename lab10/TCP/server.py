import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Server ------------------') 

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind((serverName, serverPort ))

serverSocket.listen(1)

while True:
    print("Server waiting for connection...")
    clientSocket, addr = serverSocket.accept()
    print("Client connected from",addr)
    while True:
        data = clientSocket.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break

        filename = data.decode('utf-8')
        print(f'Received Filename: {filename}')
        try:
            with open(filename, 'r') as f:
                data = f.read()
                data = bytes(data, 'utf-8')
                f.close()
        except:
            data = bytes(f'File {filename} not found', 'utf-8')

        try:
            clientSocket.sendall(data)
            print(f'Sent to Client: {data}')
            print()
        except:
            print("Client Exited.")
    clientSocket.close()
