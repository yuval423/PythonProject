
import socket
import struct

SERVER_IP = '127.0.0.1'
SERVER_PORT = 20017
HEADER_LEN = 2

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))

        while True:
            msg = input("Enter message: ")
            client_socket.send(msg.encode())

            net_len = client_socket.recv(HEADER_LEN)
            packet_len = socket.ntohs(struct.unpack('H', net_len)[0])
            answer = client_socket.recv(packet_len).decode()
            print(answer)

            if answer.strip().upper() == "BYE":
                break

    except socket.error as msg:
        print(msg)

    finally:
        client_socket.close()


if __name__ == '__main__':
    main()