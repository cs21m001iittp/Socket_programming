import socket
import sys
#s - server socket, c- client socket, by default for ip is ipvfour, for port - TCP
s= socket.socket()
print("Socket Created")

#always use free port, range of port no.is 0 to 65three55
s.bind(('localhost',9999)) #binding ip address with port no.

s.listen(3)#server from client and three define server upto three client requent because we don't have that much space , forth clients came then server refuse it.
print("Waiting for connections")
mess = "Thank for joining me "

#if i will first request then process it, then get second request and process it...and so on(so use loop)
while True:
    c, addr = s.accept() #here server accept the client request it return socket of client and ip address
    print("Connected with ", addr)

    #c.send(bytes("Welcome to GOFS,", 'utf-8'))#we have to send in byte format, not in string format
    c.send(bytes(mess.encode('utf-8')))
    while True:
        
        data = c.recv(1024).decode()
        if not data or data == 'END':
            break
        print("Received fron client side :%s"%data)
        
        data = input("You want to say anything to client : ")
        if data.lower() == 'y':
            mess = input("Enter your message: ")
        else:
            break
        try:
            c.send(bytes(mess.encode('utf-8')))
        except:
            print("Exited by user")
    c.close()

