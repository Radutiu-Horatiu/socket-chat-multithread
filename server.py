import socket
from threading import Thread

# handle connection of client
def handleConnection(s, i):
    # receive reply
    reply = s.recv(1024).decode("utf-8")
    print("Client: " + reply)

    # send message
    message = input("Server: ")
    s.send(str(message).encode("utf-8"))

# setting up socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
i = 0

# keep threads running
while True:
    i += 1
    cs,addr = s.accept()
    t = Thread(target = handleConnection, args = (cs, i))
    t.start()