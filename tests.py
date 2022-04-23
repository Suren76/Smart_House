import socket
import requests


site_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site_server.bind(('', 80))
site_server.listen(5)



conn, addr = site_server.accept()
conn.settimeout(3.0)
print('Got a connection from %s' % str(addr))
request = conn.recv(1024)
conn.settimeout(None)
request = str(request)
print('Content = %s' % request)
relay_on = request.find('/?relay=on')
relay_off = request.find('/?relay=off')
url_get_value = request.split()
print(url_get_value)