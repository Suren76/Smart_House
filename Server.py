class Server:
    import socket, time

    def __init__(self, address, port):
        self.server = self.socket.socket(self.socket.AF_INET, self.socket.SOCK_STREAM)
        self.server.bind((address, port))
        self.server.listen()
        self.address_list = []
        self.name = None

    def accept(self):
        return self.server.accept()

    def data(self):
        data = self.server.recv(1024)
        return data.decode("utf-8")

    def send_msg(self, message):
        message = message.encode("utf-8")
        self.server.sendall(message)

    def mode_connection(self, end):
        print(end)
        while not end:
            conn, address = self.server.accept()
            with conn:
                print(address)
                conn.send(str(address).encode("utf-8"))
                # self.send_msg("666666666666")
                self.address_list.append(conn)
                print(self.address_list)
                # self.server.send(address)

    def mode_data(self):
        for conn in self.address_list:
            conn.send("data_mode")




