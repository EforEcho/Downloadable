import socket

class Client:
    def __init__(self, IP) -> None:
        self.PORT = 5050
        self.IP = IP
        self.HEADER_LENGTH = 64
        self.FORMAT = "utf-8"

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect((self.IP, self.PORT))

    def send(self, msg) -> None:
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER_LENGTH - len(send_length))

        self.client_socket.send(send_length)
        self.client_socket.send(message)