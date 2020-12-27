import socket

serverName = '127.0.0.1'
serverPort = 54321

print('------------------ Server ------------------') 

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind((serverName, serverPort ))

print("UDP server up and listening")

while True:
    data,addr = serverSocket.recvfrom(1024)
    if not data or data.decode('utf-8')=='END':
        break

    filename = data.decode('utf-8')
    print(f'Received Filename: {filename} From: {addr}')
    try:
        with open(filename, 'r') as f:
            data = f.read()
            data = bytes(data, 'utf-8')
            f.close()
    except:
        data = bytes(f'File {filename} not found', 'utf-8')

    serverSocket.sendto(data,addr)
    print(f'Sent: {data} To: {addr}')
    print()
serverSocket.close()
