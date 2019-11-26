from socket import *
from threading import *


class PyClientSocket:

    def __init__(self):
        # Client Socket
        self.PySocket = None

        # Receive Message Thread
        self.AcceptThread = None

    def connect_to_server(self, setScreenText):
        self.PySocket = socket(AF_INET, SOCK_STREAM)

        try:
            self.PySocket.connect(("127.0.0.1", 8081))
        except error:
            print("서버 접속 실패: " + error)
            return False

        print("서버 접속 완료")

        while True:
            setScreenText = self.PySocket.recv(256).decode("UTF-8")

        return True

    def accept_thread(self):
        self.AcceptThread = Thread(target=self.thread_body, args=())
        self.AcceptThread.start()

    def send_message(self, message):
        def message_handle():
            self.PySocket.send(message.encode("UTF-8"))
            print("메세지 전송!" + message)
        return message_handle


