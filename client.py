import socket

c =socket.socket()
c.connect(('localhost', 9999))#server will bind the ip and port, client ony connect to particular server(ipaddress and port)
#buff = c.recv(1024).decode()

#print(buff)

#while True:
    #c.send(bytes("ok i got it",'utf-8'))
    #c.send(bytes("one",'utf-8'))
    #c.send(bytes("two",'utf-8'))
    #c.send(bytes("three",'utf-8'))

mess = "Thanks for accept my request"
c.send(mess.encode('utf-8'))
try:
    while True:
        
        data = c.recv(1024).decode()
        print("Recieved from server : %s"%data)
        more_data = input("You want send more data to server : ")
        if more_data.lower() == 'y':
            mess = input("Enter your message ")
        else:
            break
        try:
            c.send(bytes(mess.encode('utf-8')))
        except:
            print("Exited by user")
except KeyboardInterrupt:
    print("Exited by user")
c.close()