# -*- coding:utf-8 -*- 

"""
Crie um programa em python que se conecta via socket na porta 443 e envia 
a frase "Hacking Dojo", entao faça com que este programa 
seja executado dentro da VM do Windows 10 envie a frase para o handler. 
"""

import socket 

host, port = '127.0.0.1', 443


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.sendall(b"Hacking Dojo")
                       
