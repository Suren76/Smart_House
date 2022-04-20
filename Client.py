class Client:

    import socket

    def __init__(self):
        self.client = self.socket.socket(self.socket.AF_INET, self.socket.SOCK_STREAM)

    def connect(self, address, port):
        self.client.connect((address, port))

    def data(self):
        return self.client.recv(1024).decode("utf-8")

    def send(self, message):
        message = message.encode("utf-8")
        self.client.sendall(message)






