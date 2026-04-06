import socket
import os

HOST = 'localhost'
PORT = 10389
PASTA_DOWNLOADS = "downloads"

os.makedirs(PASTA_DOWNLOADS, exist_ok=True)


def baixar_arquivo(sock, nome):
    """Recebe um arquivo enviado pelo servidor."""
    resposta = sock.recv(256).decode()

    if resposta.startswith("ERRO:"):
        print(f"  [!] {resposta.split(':', 1)[1]}")
        return

    tamanho = int(resposta.split(":")[1])
    sock.send("PRONTO".encode())

    caminho = os.path.join(PASTA_DOWNLOADS, nome)
    recebido = 0

    with open(caminho, "wb") as f:
        while recebido < tamanho:
            bloco = sock.recv(4096)
            if not bloco:
                break
            f.write(bloco)
            recebido += len(bloco)

    print(f"  [+] Arquivo '{nome}' salvo em '{PASTA_DOWNLOADS}/'")


def enviar_arquivo(sock, nome):
    """Envia um arquivo local para o servidor."""
    if not os.path.exists(nome):
        print(f"  [!] Arquivo '{nome}' não encontrado localmente.")
        sock.send("TAM:0".encode())
        sock.recv(16)  # descarta resposta de erro
        return

    tamanho = os.path.getsize(nome)
    sock.send(f"TAM:{tamanho}".encode())

    ack = sock.recv(16).decode()
    if ack != "PRONTO":
        print("  [!] Servidor recusou o envio.")
        return

    with open(nome, "rb") as f:
        while True:
            bloco = f.read(4096)
            if not bloco:
                break
            sock.sendall(bloco)

    confirmacao = sock.recv(256).decode()
    print(f"  [+] {confirmacao}")


# ── CONEXÃO ───────────────────────────────────────────────────────────────────

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((HOST, PORT))
    print(f"[CLIENTE] Conectado ao servidor {HOST}:{PORT}\n")

    boas_vindas = cliente.recv(1024).decode()
    print(f"Servidor: {boas_vindas}\n")

    while True:
        comando = input(">>> ").strip()
        if not comando:
            continue

        cliente.send(comando.encode())

        # QUIT
        if comando.upper() == "QUIT":
            cliente.recv(1024)
            print("[CLIENTE] Conexão encerrada.")
            break

        # BAIXAR
        elif comando.upper().startswith("BAIXAR "):
            nome = comando[7:].strip()
            baixar_arquivo(cliente, nome)

        # ENVIAR
        elif comando.upper().startswith("ENVIAR "):
            nome = comando[7:].strip()
            enviar_arquivo(cliente, nome)

        # CHAT
        elif comando.upper().startswith("CHAT "):
            resposta = cliente.recv(1024).decode()
            if resposta.startswith("CHAT "):
                print(f"Servidor (chat): {resposta[5:]}")
            else:
                print(f"Servidor: {resposta}")

        # MENU, LISTAR e outros
        else:
            resposta = cliente.recv(4096).decode()
            print(f"Servidor:\n{resposta}\n")

except ConnectionRefusedError:
    print("[CLIENTE] ERRO: Servidor não encontrado. Execute o servidor primeiro!")

except KeyboardInterrupt:
    print("\n[CLIENTE] Interrompido.")

finally:
    cliente.close()