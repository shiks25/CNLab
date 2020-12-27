import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Client ------------------')

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

try:
    while True:
        filename = input('Enter file name: ')

        if not filename: 
            break

        clientSocket.sendall(bytes(filename, 'utf-8'))
        print(f'Sent: {filename}')

        data = clientSocket.recv(1024)
        contents = data.decode('utf-8')
        print(f'Received from Server:\n{contents}')
        print()
        
except KeyboardInterrupt:
    print("Client Exited.")
clientSocket.close()
