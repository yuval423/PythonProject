import socket
import struct
import datetime
import random

IP = '0.0.0.0'
PORT = 21112
QUEUE_SIZE = 1
MAX_PACKET = 4
LEN_SIGN = 'H'


def get_answer(command):
    # decide what to answer for every command
    if command == "":
        return "invalid"
    if command == "TIME":
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif command == "NAME":
        return "YUVAL"
    elif command == "RAND":
        return str(random.randint(1, 10))
    elif command == "EXIT":
        return "bye"
    else:
        return "invalid"


def send_with_length(sock, msg):
    # sends length and then the message
    packet_len = socket.htons(len(msg))
    sock.send(struct.pack(LEN_SIGN, packet_len))
    sock.send(msg.encode())


def main():
    # create server socket and listen for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(QUEUE_SIZE)

    while True:
        try:
            # accept a new client
            comm_socket, client_address = server_socket.accept()

            while True:
                # get command from client
                data = comm_socket.recv(MAX_PACKET).decode().strip()

                # get response for command
                answer = get_answer(data)

                # send answer
                send_with_length(comm_socket, answer)

                # if commend = EXIT we stop serving this client
                if answer == "bye":
                    break

        except socket.error as msg:
            # error handling
            print("server socket error:", msg)

        finally:
            # close this client's socket
            comm_socket.close()


if __name__ == '__main__':
    main()