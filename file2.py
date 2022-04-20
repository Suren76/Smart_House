import Server
import os

server = Server.Server("127.0.0.11", 9999)
server.name = "server1"

os.system(f"export SERVER={server}")


while input() != "quit":
    print(1)
    server.name = input()