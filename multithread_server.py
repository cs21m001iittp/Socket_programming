import socket
import sys
from _thread import *
from threading import Thread, Lock

#localhost = "10.21.211.151"

mutex = Lock()
server_socket = socket.socket()
print("Socket Created ")
threadCount = 0
dict = {}
server_socket.bind(('localhost',9999)) #binding ip address with port no.

server_socket.listen(3)#server from client and three define server upto three client requent because we don't have that much space , forth clients came then server refuse it.
print("Waiting for connections")
mess = "Thank for joining me "

def client_thread(connection):
    connection.send(mess.encode())
    while True: 
        msg = connection.recv(2048).decode()
        #reply = "Hello , I am server : "+ data.decode('utf-8')
        #if not data:
            #break
        #connection.sendall(str.encode(reply))
        data = msg.split(',')
        mutex.acquire()
        dict[data[0]]= data[1]
        print(dict)
        mutex.release()
        connection.send(str.encode("bsdk"))
        
    connection.close()


while True:
    client, addr = server_socket.accept()
    print("Connected to : "+addr[0] +" "+ str(addr[1]))
    start_new_thread(client_thread,(client,))#start_new_thread  is function for create thread
    threadCount +=1
    print("ThreadCount"+str(threadCount))
server_socket.close()