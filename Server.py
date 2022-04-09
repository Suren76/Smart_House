class Server:
    import socket, time

    def __init__(self, address, port):
        self.server = self.socket.socket(self.socket.AF_INET, self.socket.SOCK_STREAM)
        self.server.bind((address, port))
        self.server.listen()
        self.address_list = []

    def accept(self):
        return self.server.accept()

    def data(self):
        data = self.server.recv(1024)
        return data.decode("utf-8")

    def send(self, message):
        message = message.encode("utf-8")
        self.server.sendall(message)

    def mode_connection(self, end):
        while not end:
            conn, address = self.server.accept()
            with conn:
                print(address)
                conn.send(address)
                self.address_list.append(conn)
                # self.server.send(address)

    def mode_data(self):
        for conn in self.address_list:
            conn.send("data_mode")




