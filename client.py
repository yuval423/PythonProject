"""
author - yuval agami
date   - 1.11.25
"""
#יבוא מודלים
import socket
import struct
#הגדרת קבועים
SERVER_IP = '127.0.0.1'
SERVER_PORT = 20017
HEADER_LEN = 2

def main():# יצירת socket חדש
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))

        while True:#קליטת הודעה
            msg = input("Enter message: ")
            client_socket.send(msg.encode())
            net_len = client_socket.recv(HEADER_LEN)#קבלת 2 בייטים מהשרת פירוק stuct H
            packet_len = socket.ntohs(struct.unpack('H', net_len)[0])
            answer = client_socket.recv(packet_len).decode()#פיענוך ההודעה ולהדפיס אותה
            print(answer)

            if answer.strip().upper() == "BYE":
                break# אם ההודעה היא ביי אז לצאת מהלולאה

    except socket.error as msg:#תפיסת שגיאה
        print(msg)

    finally:
        client_socket.close()#סגירת הסוקט


if __name__ == '__main__':
    main()