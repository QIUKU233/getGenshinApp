import socket
import time
import simpleGenshineGetResinsApi
# IP是对方IP
IP = "" 
# 对方端口
PORT = 7788

def makemsg():
    msg = simpleGenshineGetResinsApi.main()
    return ','.join(msg)
def send_msg(udp_socket):
    """发送消息"""
    dest_ip = IP
    dest_port = PORT
    send_data = makemsg()
    print(send_data)
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip, dest_port))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定消息
    udp_socket.bind(("", 2020))

    # 循环进行处理，发送和接收
    while True:
        send_msg(udp_socket)
        time.sleep(100)

if __name__ == '__main__':
    main()