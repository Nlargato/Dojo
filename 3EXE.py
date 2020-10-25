# -*- coding:utf-8 -*- 

"""
 3 - Crie uma condicional no seu programa que ao receber a string "Dojo" escreva o conteúdo recebido em um arquivo de texto chamado log + data + hora + ip de origem do envio.txt por exemplo log-04062020-0344-192-168-1-3.txt 
"""



import datetime
import socket
import os
from _thread import *
import re


address = list()
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
        
        elif re.search('Dojo', str(data)):

            now = datetime.datetime.now()
            nowstr = now.strftime("%d%m%Y%H%M")


            ipAddr = address[0]
            ipAddr = ipAddr.replace('.','')

            filename = 'log{}{}.txt'.format(nowstr, ipAddr)
            path = "echo '{}' > {}".format(str(data), filename)
            os.system(path)

        connection.sendall(str.encode(response)) 
    
    connection.close()                                                                                                                                                                                                                     
 


while True:                                                                                                                                                                                                                                
    Client, address = ServerSideSocket.accept()                                                                                                                                                                                            
    print('Connected to: ' + address[0] + ':' + str(address[1]))                                                                                                                                                                           
    start_new_thread(multi_threaded_client, (Client, ))                                                                                                                                                                                    
    ThreadCount += 1                                                                                                                                                                                                                       
    print('Thread Number: ' + str(ThreadCount))                                                                                                                                                                                            
                                                                                                                                                                                                                                           
ServerSideSocket.close()                                                                                                                                                                                                                   
                        
