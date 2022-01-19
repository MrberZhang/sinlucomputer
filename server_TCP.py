# TCP 服务端结构：
import socket

tcps = socket.socket()   # 创建服务器套接字
tcps.bind()      # 把地址绑定到套接字
tcps.listen()      # 监听链接
while True:      # 服务器无限循环
    tcpc = tcps.accept()  # 接受客户端链接
    while True:         # 通讯循环
        tcpc.recv()/tcpc.send()  # 对话(接收与发送)
    tcpc.close()    # 关闭客户端套接字
tcps.close()        # 关闭服务器套接字(可选)
