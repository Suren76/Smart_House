# Complete project details at https://RandomNerdTutorials.com
import dht
# [{"humidity": 0, "temperature": 0, "sensor": "dht", "time": [2022, 4, 23, 5, 59, 0, 5, 113], "name": "nodemcu_multisensor"}, {"time": [2022, 4, 23, 5, 59, 0, 5, 113], "status": "off", "name": "nodemcu_multisensor", "sensor": "relay"}]

def web_page(name=name):
    if relay.value() == 1:
        relay_state = ''
    else:
        relay_state = 'checked'
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    html = """<!DOCTYPE HTML><html><head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style> html { font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }
    .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:none}
  .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
  .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
  input:checked+.slider{background-color:#2196F3}
  input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
    h2 { font-size: 3.0rem; } p { font-size: 3.0rem; } .units { font-size: 1.2rem; } 
    .ds-labels{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
  </style><script>function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); if(element.checked){ xhr.open("GET", "/?relay=on", true); }
  else { xhr.open("GET", "/?relay=off", true); } xhr.send(); }</script></head>
  <body><h2>ESP with DHT-11 </h2>
  <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="ds-labels">Temperature</span>
    <span id="temperature">""" + str(temp) + """</span>
    <sup class="units">&deg;C</sup>
  </p>
    <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="ds-labels">Humidity</span>
    <span id="humidity">""" + str(humidity) + """</span>
    <sup class="units">%</sup>
  </p>
  <p><h1>ESP Relay Web Server</h1><label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" """ +relay_state+ """><span class="slider">
  </span></label>
  </p>
  <p> """+str(name)+""" </p>
  </body></html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
relay.value(0)
status = "off"

if run_mode == "main":
    while True:
        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = s.accept()
            conn.settimeout(3.0)
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            print('Content = %s' % request)
            relay_on = request.find('/?relay=on')
            relay_off = request.find('/?relay=off')

            url_get_value = request.split()[1].split("/")
            if url_get_value[0] == '' and url_get_value[1] == "name" and url_get_value[2][:7] == "nodemcu":
                with  open("config.json", "w+") as file:
                    file.write(json.dumps({'name': str(url_get_value[2])}))
                name = str(url_get_value[2])

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
            sensor.measure()
            local_time = time.localtime()
            time_now = str(local_time[0])+"."+str(local_time[1])+"."+str(local_time[2])+" "+str(local_time[3])+":"+str(local_time[4])+":"+str(local_time[5])
            response = json.dumps([{"sensor": "dht", "name":name, "time": time_now, "humidity": sensor.humidity(), "temperature": sensor.temperature()},
                                   {"sensor": "relay", "name":name, "time": time_now, "status": status}])
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
            conn, addr = s.accept()
            conn.settimeout(3.0)
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            print('Content = %s' % request)
            relay_on = request.find('/?relay=on')
            relay_off = request.find('/?relay=off')

            url_get_value = request.split()[1].split("/")
            if url_get_value[0] == '' and url_get_value[1] == "name" and url_get_value[2][:7] == "nodemcu":
                with  open("config.json", "w+") as file:
                    file.write(json.dumps({'name': str('nodemcu_' + ip)}))
                name = str('nodemcu_' + ip)

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
