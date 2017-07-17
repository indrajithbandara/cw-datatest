# -*- coding: utf-8 -*-
import socket
import struct
import sqlalchemy
import pandas
########################################################################
class sckt:
    #----------------------------------------------------------------------
    def __init__(self, host = '192.168.1.3', port = 12345):
        self.host = host
        self.port = port
    #----------------------------------------------------------------------
    def run_server(self):
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.bind((self.host, self.port))
        sckt.listen(5)
        """连接库"""
        engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@XiTongDSN')
        """取开盘价"""
        Open = (pandas.read_sql('sh', engine))['open']
        i = 0
        while True:            
            connection, address = sckt.accept()
            if connection.recv(1024) == b'Link' and i < (len(Open) - 1):               
                """数据打包"""                
                connection.send(struct.pack('f', Open[i]))
                i += 1
            else:
                connection.send(b'Cut off the connection!')
                connection.close()
    #----------------------------------------------------------------------
    def run_client(self, message = b'Link'):
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.connect((self.host, self.port))
        sckt.send(message)
        """数据解包，注意 unpack 要求四字节，其用法为后接 [:4]"""
        Open = struct.unpack('f', sckt.recv(1024)[:4])
        sckt.close()
        """返回开盘价，去格式的用法后接 [0]"""
        return Open[0]