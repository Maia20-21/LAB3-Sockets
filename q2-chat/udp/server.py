import socket

HOST = '127.0.0.1' 
PORT = 10436

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM para UDP
server.bind((HOST, PORT)) 

print(f"Servidor UDP aguardando mensagens em {PORT}...")

while True: 
    msg, addr = server.recvfrom(1024)
    msg = msg.decode()
    
    if msg == "QUIT":
        print("O cliente encerrou o chat.")
        break
        
    print(f"Cliente disse: {msg}")
    
    resposta = input("Servidor: ")
    server.sendto(resposta.encode(), addr)
    
    if resposta.upper() == "QUIT":
        print("Você encerrou o chat.")
        break

server.close()
