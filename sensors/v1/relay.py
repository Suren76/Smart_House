########################      relay     ####################################################################
def web_page():
  if relay.value() == 1:
    relay_state = ''
  else:
    relay_state = 'checked'
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
  body{font-family:Arial; text-align: center; margin: 0px auto; padding-top:30px;}
  .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:none}
  .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
  .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
  input:checked+.slider{background-color:#2196F3}
  input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
  </style><script>function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); if(element.checked){ xhr.open("GET", "/?relay=on", true); }
  else { xhr.open("GET", "/?relay=off", true); } xhr.send(); }</script></head><body>
  <h1>ESP Relay Web Server</h1><label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" %s><span class="slider">
  </span></label></body></html>""" % (relay_state)
  return html


status = "off"

site_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site_server.bind(('', 80))
site_server.listen(5)



if run_mode == "main":
    while True:
        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = site_server.accept()
            conn.settimeout(3.0)
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            
            nodemcu_name()
            
            print('Content = %s' % request)
            relay_on = request.find('/?relay=on')
            relay_off = request.find('/?relay=off')

            if relay_on == 6:
              print('RELAY ON')
              relay.value(0)
              led.value(0)
              status = "on"
            if relay_off == 6:
              print('RELAY OFF')
              relay.value(1)
              led.value(1)
              status = "off"
            
            local_time = time.localtime()
            time_now = str(local_time[0])+"."+str(local_time[1])+"."+str(local_time[2])+" "+str(local_time[3])+":"+str(local_time[4])+":"+str(local_time[5])
            response = json.dumps({"sensor": "relay", "name":name, "time": time_now, "status": status})
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as e:
            conn.close()
            print('Connection closed')

if run_mode == "reserve":
    while True:
        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = site_server.accept()
            conn.settimeout(3.0)
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            
            nodemcu_name()
            
            print('Content = %s' % request)
            relay_on = request.find('/?relay=on')
            relay_off = request.find('/?relay=off')

            if relay_on == 6:
              print('RELAY ON')
              relay.value(0)
              led.value(0)
            if relay_off == 6:
              print('RELAY OFF')
              relay.value(1)
              led.value(1)
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as e:
            conn.close()
            print('Connection closed')


if run_mode == "quit":
    quit()



