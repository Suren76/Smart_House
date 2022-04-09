# import time, machine, dht, network, socket
#
# sensor = dht.DHT11(machine.Pin(4))
#
# html = f"""<!DOCTYPE html>
# <html>
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <meta http-equiv="X-UA-Compatible" content="ie=edge">
#   <title>Home</title>
#   <link rel="icon" type="image/x-icon" href="img/logo/go_logo1_bxc_icon.ico">
#   <link rel="stylesheet" href="css/style.css">
#   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
#   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
# </head>
# <body>
#
#   <header class="pb-5 mb-3">
#     <nav class="shadow bg-body navbar navbar-expand-sm navbar-light bg-light fixed-top">
#       <div class="container">
#
#         <a href="" class="navbar-brand" id="logo">
#           <img src="" id=logo class="me-3">
#           Smart House
#         </a>
#
#         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" >
#           <span class="navbar-toggler-icon"></span>
#         </button>
#
#         <div class="collapse navbar-collapse justify-content-center" id="navbarContent">
#           <ul class="navbar-nav ms-auto text-center ">
#             <li class="nav-item mx-1">
#               <a href="/" class="nav-link">Home</a>
#             </li>
#             <li class="nav-item mx-1">
#               <a href="/about.html" class="nav-link">Scenario</a>
#             </li>
#             <li class="nav-item mx-1">
#               <a href="/Settings.html" class="nav-link">Settings</a>
#             </li>
#             <li class="nav-item mx-1">
#               <a href="/about.html" class="nav-link">About Us</a>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>
#   </header>
#
#   <main class="pt-3">
#     <div class="container sensors-list p-3 text-center">
#       <div class="row">
#         <div class="col-6 col-sm-6 col-md-4 ">
#           <div class="sensor-block">
#             <h5>Temperature</h5>
#             <div class="sensor-data">
#               {sensor.humidity()}
#             </div>
#             <a href="" class="btn">more</a>
#           </div>
#         </div>
#         <div class="col-6 col-sm-6 col-md-4">
#           <div class="sensor-block">
#             <h5>Humidity</h5>
#             <div class="sensor-data">
#               {sensor.temperature()}
#             </div>
#             <a href="" class="btn">more</a>
#           </div>
#         </div>
#         <div class="col-6 col-sm-6 col-md-4">
#           <div class="sensor-block">
#             <h5>Light</h5>
#             <div class="sensor-data">
#               main data
#             </div>
#             <a href="" class="btn">more</a>
#           </div>
#         </div>
#       </div>
#     </div>
#
#   </main>
#   <footer class=" mt-md-5 pb-md-5 border-top footer-bg">
#     <div class=" container-fluid">
#       <div class="row justify-content-center">
#         <!-- <div class="col-sm-1 "></div>
#         <div class="col-8 col-md col-sm-4 text-center">
#           <div class="contact-info pt-3">
#             <div class="tell my-1"><i class="bi bi-telephone"></i></div>
#             <div class="email my-1"><i class="bi bi-envelope">   parsyansuren.work@gmail.com</i></div>
#             <div class="address my-1 mt-3"><i class="bi bi-geo-alt"></i></div>
#           </div>
#         </div> -->
#
#         <div class="col-7 col-md text-center justify-content-center mt-5 pt-5">
#             <ul class="nav justify-content-center border-bottom border-dark pb-3 mb-3 footer-menu">
#               <li class="nav-item"><a href="/" class="nav-link px-2 text ">Home</a></li>
#               <li class="nav-item"><a href="/about.html" class="nav-link px-2 text ">About Us</a></li>
#             </ul>
#
#             <ul class="list-unstyled d-flex justify-content-center mt-5">
#                <li class="ms-3">
#                  <a class="link-dark" href="https://www.facebook.com/profile.php?id=100009193080852">
#                    <i class="bi bi-facebook icon"></i>
#                  </a>
#                </li>
#
#                <li class="ms-3">
#                  <a class="link-dark" href="https://www.facebook.com/messages/t/100009193080852/">
#                    <i class="bi bi-messenger icon"></i>
#                  </a>
#                </li>
#
#                <li class="ms-3">
#                  <a class="link-dark" href="https://www.github.com/Suren76">
#                    <i class="bi bi-github icon"></i>
#                  </a>
#                </li>
#             </ul>
#             <div class="footer-about my-1 mt-5 pt-3">
#               <h5 class="my-2">About Project</h5>
#               "Smart House" project owned by <a href="">Me</a><br>
#               for Digicode2022
#
#             </div>
#
#         </div>
#       </div>
#     </div>
#   </footer>
#
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
# </body>
# </html>
# """
#
#
# HOST = ""  # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             conn.sendall("""Connected""")
#             conn.sendall(html)
#             print(data)
#
#
#
#
# while True:
#     sensor.measure()
#     print("Humidity: ", )
#     print("Temperature: ", )
#     time.sleep(1)
k = 0xFF

while True:
    if k == ord('q'):
        print("q")