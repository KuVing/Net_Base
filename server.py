# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:39:22 2021

@author: 15003
"""
import socket
def main():
    s=socket.socket()
    host=socket.gethostname()    #获取IP地址
    port=12345                   #通信端口
    s.bind((host,port))           #绑定IP地址和端口  
    s.listen(5)                  
    c,addr=s.accept()            #建立连接。C是客户套接字，addr是对方IP
    print("对方地址是：",addr)    

    c.send("welcome".encode("UTF-8"))
    print(c.recv(1024).decode("utf-8"))
    c.close()

if __name__=="__main__":
    main()