import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print ("El nombre tu ordenador es: " +  hostname)
print ("Tu direccion IP: " + ip)