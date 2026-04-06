import socket

HOST = '127.0.0.1'
PORT = 10431

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Cliente: ")
    client.send(msg.encode())

    if msg == "QUIT":
        break

    resp = client.recv(1024).decode()
    print("Servidor:", resp)

    if resp == "QUIT":
        break

client.close()