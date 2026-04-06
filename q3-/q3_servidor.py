import socket
import os

HOST = 'localhost'
PORT = 10389
PASTA_ARQUIVOS = "arquivos_servidor"

os.makedirs(PASTA_ARQUIVOS, exist_ok=True)

# Cria um arquivo de exemplo na pasta do servidor
exemplo = os.path.join(PASTA_ARQUIVOS, "exemplo.txt")
if not os.path.exists(exemplo):
    with open(exemplo, "w") as f:
        f.write("Olá! Este é um arquivo de exemplo do servidor.\n")
        f.write("Redes de Computadores - Mackenzie\n")


def listar_arquivos():
    return os.listdir(PASTA_ARQUIVOS)


def enviar_arquivo(conexao, nome):
    """Envia arquivo do servidor para o cliente."""
    caminho = os.path.join(PASTA_ARQUIVOS, nome)
    if not os.path.exists(caminho):
        conexao.send("ERRO:Arquivo não encontrado no servidor.".encode())
        return

    tamanho = os.path.getsize(caminho)
    conexao.send(f"OK:{tamanho}".encode())

    confirmacao = conexao.recv(16).decode()
    if confirmacao != "PRONTO":
        return

    with open(caminho, "rb") as f:
        while True:
            bloco = f.read(4096)
            if not bloco:
                break
            conexao.sendall(bloco)

    print(f"  [+] Arquivo '{nome}' enviado ao cliente.")


def receber_arquivo(conexao, nome):
    """Recebe arquivo enviado pelo cliente."""
    info = conexao.recv(64).decode()

    if not info.startswith("TAM:"):
        conexao.send("ERRO".encode())
        return

    tamanho = int(info.split(":")[1])

    if tamanho == 0:
        conexao.send("ERRO".encode())
        print(f"  [!] Cliente informou que o arquivo '{nome}' não existe localmente.")
        return

    conexao.send("PRONTO".encode())

    caminho = os.path.join(PASTA_ARQUIVOS, "recebido_" + nome)
    recebido = 0

    with open(caminho, "wb") as f:
        while recebido < tamanho:
            bloco = conexao.recv(4096)
            if not bloco:
                break
            f.write(bloco)
            recebido += len(bloco)

    print(f"  [+] Arquivo salvo como 'recebido_{nome}'.")
    conexao.send(f"Arquivo '{nome}' recebido com sucesso!".encode())


# ── INICIALIZAÇÃO ─────────────────────────────────────────────────────────────

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"[SERVIDOR] Rodando em {HOST}:{PORT}")
print(f"[SERVIDOR] Pasta de arquivos: '{PASTA_ARQUIVOS}/'")
print("[SERVIDOR] Aguardando cliente...\n")

conexao, endereco = servidor.accept()
print(f"[SERVIDOR] Cliente conectado: {endereco}\n")

conexao.send("Conectado! Digite MENU para ver os comandos disponíveis.".encode())

while True:
    dados = conexao.recv(1024)
    if not dados:
        print("[SERVIDOR] Cliente desconectou.")
        break

    comando = dados.decode().strip()
    print(f"[Cliente]: {comando}")

    # QUIT
    if comando.upper() == "QUIT":
        conexao.send("QUIT".encode())
        print("[SERVIDOR] Encerrando...")
        break

    # MENU
    elif comando.upper() == "MENU":
        menu = (
            "\n=== MENU ===\n"
            "LISTAR          - Lista arquivos disponíveis no servidor\n"
            "BAIXAR <arq>    - Baixa um arquivo do servidor\n"
            "ENVIAR <arq>    - Envia um arquivo ao servidor\n"
            "CHAT <mensagem> - Envia mensagem de chat\n"
            "QUIT            - Encerra a conexão\n"
        )
        conexao.send(menu.encode())

    # LISTAR
    elif comando.upper() == "LISTAR":
        arquivos = listar_arquivos()
        if arquivos:
            resposta = "Arquivos no servidor:\n" + "\n".join(f"  - {a}" for a in arquivos)
        else:
            resposta = "Nenhum arquivo disponível."
        conexao.send(resposta.encode())

    # BAIXAR (servidor envia pro cliente)
    elif comando.upper().startswith("BAIXAR "):
        nome = comando[7:].strip()
        enviar_arquivo(conexao, nome)

    # ENVIAR (cliente manda pro servidor)
    elif comando.upper().startswith("ENVIAR "):
        nome = comando[7:].strip()
        receber_arquivo(conexao, nome)

    # CHAT
    elif comando.upper().startswith("CHAT "):
        mensagem = comando[5:]
        print(f"  [CHAT do cliente]: {mensagem}")
        resposta = input("  Sua resposta (servidor): ")
        conexao.send(f"CHAT {resposta}".encode())

    else:
        conexao.send("Comando inválido. Digite MENU para ver as opções.".encode())

conexao.close()
servidor.close()
print("[SERVIDOR] Encerrado.")
