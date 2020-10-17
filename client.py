import socket

# we want to keep chatting
while True:
    # connection to server
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",7777))

    # sending messages
    msg = input("Client: ")
    s.send(str(msg).encode())

    # printing received messages
    reply = s.recv(1024).decode("utf-8")
    print("Server: " + reply)