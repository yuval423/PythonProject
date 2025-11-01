import socket
import struct
import datetime
import random

IP = '0.0.0.0'
PORT = 20017
QUEUE_SIZE = 1
MAX_PACKET = 4
LEN_SIGN = 'H'


def main():#האזנה ללקוח קישור לפורט ויצירת סוקט
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(QUEUE_SIZE)

    while True:
        try:#לולאה שמקבלת קליינט חדש כל פעם
            comm_socket, client_address = server_socket.accept()

            while True:#לולאה פנימית מקבלת פקודה מהקליינט שעכשיו
                request = comm_socket.recv(MAX_PACKET).decode().strip()
#בדיקת הפקודה ושלחת התשובה המתאימה לפקודה
                if request == "TIME":
                    answer = datetime.datetime.now().strftime("%H:%M:%S")
                elif request == "NAME":
                    answer = "YUVAL"
                elif request == "RAND":
                    answer = str(random.randint(1, 10))
                elif request == "EXIT":
                    answer = "bye"
                else:
                    answer = "invalid"
#שליחת אורך ההודעה ואז שליחת ההודעה עצמה
                packet_len = socket.htons(len(answer))
                comm_socket.send(struct.pack(LEN_SIGN, packet_len))
                comm_socket.send(answer.encode())

                if answer == "bye":#יציאה מהלולאה הפנימית שהקליינט רושם EXIT
                    break

        except socket.error as msg:#קליטת שגיאות
            print("server socket error:", msg)

        finally:#סגירת החיבור של הקליינט הנוכחי וחוזרים ללולאה הראשית שמקבלת קליינט חדש
            comm_socket.close()



if __name__ == '__main__':
    main()