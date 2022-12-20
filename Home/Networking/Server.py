import threading
import socket
import time


class Server:
    def __init__(self) -> None:
        self.HOSTNAME = socket.gethostname()
        self.PORT = 5050
        self.IP = socket.gethostbyname(self.HOSTNAME)

        self.HEADER_LENGTH = 64
        self.FORMAT = "utf-8"

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind((self.IP, self.PORT))

        self.server_socket.listen()

    def start(self) -> None:
        print('[Starting]:\tServer is starting...')
        self.server_socket.listen()
        print('[Listening]:\tServer listening on', self.IP)

        while True:
            conn, addr = self.server_socket.accept()

            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print('[Active Connections]:\t')

    def handle_client(self, conn, addr) -> None:
        print('[Connection established]:\t')

        connected = True

        while connected:
            msg_length = conn.recv(self.HEADER_LENGTH).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                print(addr, msg)