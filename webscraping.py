import socket
import urllib.request, urllib.parse, urllib.error

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.example.com', 80))
cmd = 'GET http://www.example.com HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode().strip())
mysock.close()

print(" ")
print("THE EXAMPLE ABOVE USES THE SOCKET LIBRARY")
print(" ")

fhand = urllib.request.urlopen('http://www.example.com')
for line in fhand:
    print(line.decode().strip())

print(" ")
print("THE EXAMPLE ABOVE USES URLLIB.")
print("THE ADVANTAGE OF URLLIB IS THAT IT CAN BE TREATED LIKE A FILE.")





