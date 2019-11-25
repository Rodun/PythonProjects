from PyCPServer.CommonModule import *
from socket import *
import threading


class PyServerSocket:

    def __init__(self):
        self.ShowText = QLineEdit()
        self.message = ""

        self.PySocket = socket(AF_INET, SOCK_STREAM)
        self.PySocket.bind(("127.0.0.1", 8081))
        self.PySocket.listen(1)
        self.PySocket.settimeout(30)

        self.PyClientSocket = None
        self.PyAddress = None

        self.AcceptThread = threading.Thread(target=self.accept_threading, args=())
        self.AcceptThread.start()

        # self.AcceptThread.join()
        # print("쓰레드 종료")

    def __del__(self):
        self.PySocket.close()
        print("소켓 종료")

    def accept_threading(self):
        print("접속 대기중...")
        try:
            self.PyClientSocket, self.PyAddress = self.PySocket.accept()
        except timeout:
            print("PySocket TimeOut...")
            return

        print("[{0}]에서 접속하였습니다.".format(str(self.PyAddress)))
        self.receive_message()

    def receive_message(self):
        while True:
            data = self.PyClientSocket.recv(256)
            self.message = "[클라 receive]: " + data.decode("UTF-8")
            print(self.message)


















