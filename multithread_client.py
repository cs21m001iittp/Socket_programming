import socket
client_socket = socket.socket()

#localhost = "10.21.211.151"
print("Waiting for connection ")
client_socket.connect(('localhost', 9999))

response = client_socket.recv(1024).decode()
print(response)

while True:
    #options = input("What do you want to do : ")
    #if options == "get"
    key = input("Key :")
    value = input("Value : ")
    msg = key +","+value
    client_socket.send(str.encode(msg))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))
client_socket.close()