import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Client ------------------')

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message='Hello this is the client!'

try:
    while True:
        clientSocket.send(message.encode('utf-8'))
        data = clientSocket.recv(1024)
        print(str(data))
        more = input('Send more data to the server?Y or N\n')
        if more.lower() == 'y':
            message = input("Enter the data:\n")
        else:
            break
except KeyboardInterrupt:
    print("Client Exited.")
clientSocket.close()
