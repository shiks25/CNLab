import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Client ------------------')

UDPclientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPclientSocket.connect((serverName,serverPort))

try:
    while True:
        filename = input('Enter file name to be requested: ')

        if not filename: 
            break

        UDPclientSocket.sendall(bytes(filename, 'utf-8'))
        print(f'Sent: {filename}')

        data = UDPclientSocket.recv(1024).decode('utf-8')
        print(f'Received from Server:\n{data}')
        print()
        
except KeyboardInterrupt:
    print("Client Exited.")
UDPclientSocket.close()

