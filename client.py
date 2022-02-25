# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:46:30 2021

@author: 15003
"""

import socket
def main():
    s=socket.socket()
    host="172.22.125.232"
    port=12345  
    s.connect((host,port))
    msg=input("您要发送的内容是：")
    s.send(msg.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
    s.close()
    
if __name__=="__main__":
    main()