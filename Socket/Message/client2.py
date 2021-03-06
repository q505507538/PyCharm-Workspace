#!/usr/bin/env python
#coding: utf-8
from socket import *
from time import ctime
import select
import sys
HOST='127.0.0.1'
PORT=21569
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
input1=[tcpCliSock,sys.stdin]

while True:
  readyInput,readyOutput,readyException=select.select(input1,[],[])
  for indata in readyInput:
    if indata==tcpCliSock:
      data=tcpCliSock.recv(BUFSIZ)
      if not data:
        break
      print data
    else:
      data=raw_input()
      if not data:
        break
      tcpCliSock.send('[%s] %s' %(ctime(),data))

tcpCliSock.close()