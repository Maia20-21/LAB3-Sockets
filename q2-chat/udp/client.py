import socket

HOST = '127.0.0.1' 
PORT = 10436

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM para UDP
dest = (HOST, PORT)

while True: 
    msg = input("Cliente: ") 
    client.sendto(msg.encode(), dest)
    
    if msg == "QUIT":
        print("Você encerrou o chat.")
        break

    resposta, addr = client.recvfrom(1024)
    resposta = resposta.decode()
    
    if resposta == "QUIT":
        print("O servidor encerrou o chat.")
        break
        
    print(f"Servidor disse: {resposta}")

client.close()