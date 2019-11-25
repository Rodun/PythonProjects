from socket import *


class PyClientSocket:

    def __init__(self):
        self.PySocket = socket(AF_INET, SOCK_STREAM)
        self.PySocket.connect(("127.0.0.1", 8080))

    def send_message(self, message, encoding):
        self.PySocket.send(message.encode(encoding))

