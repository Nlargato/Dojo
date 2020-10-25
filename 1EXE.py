# -*- coding:utf-8 -*- 

"""
1 - Crie um programa em python utilizando socket que 
inicia um handler na porta 443, ou seja um processo que espera uma conexão na porta 443. 
Então deixe-o escutando no Kali. 
"""




import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 443
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening 443')                                                                                                                                             
ServerSideSocket.listen(5)                                                                                                                                                   
                                                                                                                                                                             
def multi_threaded_client(connection):                                                                                                                                       
    connection.send(str.encode(':'))                                                                                                                                         
    while True:                                                                                                                                                              
        data = connection.recv(2048)                                                                                                                                         
        response = 'ACK!\n'                                                                                                                                                  
        if not data:                                                                                                                                                         
            break                                                                                                                                                                      
        connection.sendall(str.encode(response))                                                                                                                                                                                           
    connection.close()                                                                                                                                                                                                                     
                                                                                                                                                                                                                                           
while True:                                                                                                                                                                                                                                
    Client, address = ServerSideSocket.accept()                                                                                                                                                                                            
    print('Connected to: ' + address[0] + ':' + str(address[1]))                                                                                                                                                                           
    start_new_thread(multi_threaded_client, (Client, ))                                                                                                                                                                                    
    ThreadCount += 1                                                                                                                                                                                                                       
    print('Thread Number: ' + str(ThreadCount))                                                                                                                                                                                            
                                                                                                                                                                                                                                           
ServerSideSocket.close()                                                                                                                                                                                                                   
                        
