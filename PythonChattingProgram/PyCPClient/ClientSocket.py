from socket import *


class PyClientSocket:

    def __init__(self):
        self.PySocket = None

    def connect_to_server(self):
        self.PySocket = socket(AF_INET, SOCK_STREAM)
        self.PySocket.connect(("127.0.0.1", 8081))
        print("서버 접속 완료")
        self.PySocket.send("here is it client".encode("UTF-8"))

    def send_message(self, message):
        def message_handle():
            self.PySocket.send(message.encode("UTF-8"))
            print("메세지 전송!" + message)
        return message_handle

