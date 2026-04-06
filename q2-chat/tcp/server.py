import socket

HOST = '127.0.0.1'
PORT = 10431

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor aguardando conexão...")

conn, addr = server.accept()
print("Conectado por", addr)

while True:
    msg = conn.recv(1024).decode()

    if msg == "QUIT":
        print("Cliente encerrou")
        break

    print("Cliente:", msg)

    resp = input("Servidor: ")
    conn.send(resp.encode())

    if resp == "QUIT":
        break

conn.close()
server.close()