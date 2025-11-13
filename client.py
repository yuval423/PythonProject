"""
author - yuval agami
date   - 1.11.25
"""
import socket
import struct

SERVER_IP = '127.0.0.1'
SERVER_PORT = 21112
HEADER_LEN = 2


def recv_answer(sock):
    # receive 2 bytes of length and then the message
    net_len = sock.recv(HEADER_LEN)
    packet_len = socket.ntohs(struct.unpack('H', net_len)[0])
    return sock.recv(packet_len).decode()


def main():  # create a new socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))

        while True:  # get message
            msg = input("Enter message: ")
            client_socket.send(msg.encode())

            # get answer
            answer = recv_answer(client_socket)
            print(answer)

            # if answer is bye break
            if answer.strip().upper() == "BYE":
                break

    except socket.error as msg:  # error handlingn
        print(msg)

    finally:
        client_socket.close()  # close the socket


if __name__ == '__main__':
    main()