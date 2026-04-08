# LAB 03 – Sockets TCP e UDP

## Integrantes

* Bruna Amorim Maia - RA 10431883
* Livia Negrucci Cantowitz - RA 10389419
* Rute Willemann - RA 10436781

---

## Objetivo

* Implementar e analisar comunicação cliente-servidor utilizando sockets TCP e UDP
* Comparar comportamento entre os protocolos
* Desenvolver aplicações utilizando comunicação em rede

---

## Estrutura do Projeto

```
.
├── q2-chat/
│   ├── tcp/
│   │   ├── server.py
│   │   └── client.py
│   └── udp/
│       ├── server.py
│       └── client.py
│
├── q3-aplicacao/
│   ├── server.py
│   └── client.py
│
└── respostas/
    └── questao1.txt
```

---

## Questão 1 – Análise

Arquivo: `respostas/questao1.txt`

### Resultados obtidos


a) Execute o cliente TCP antes de executar o servidor TCP. O que acontece? Por quê?  
R: Ao executar o cliente TCP antes do servidor, ocorre erro de conexão, pois o servidor não está ativo para aceitar conexões.

b) Faça o mesmo procedimento para o cliente e servidor UDP. O resultado foi similar ao socket TCP? Compare os resultados e justifique.  
R: No UDP, o cliente consegue enviar mensagens mesmo sem o servidor estar ativo, pois não há estabelecimento de conexão. Diferente do TCP, que exige conexão prévia e gera erro caso o servidor não esteja disponível.

c) O que acontece se o número da porta que o cliente tentar se conectar for diferente da porta disponibilizada pelo servidor?  
R: Se o cliente utilizar uma porta diferente da porta do servidor, a comunicação não ocorre, pois o servidor não está escutando naquela porta específica.

---

## Questão 2 – Chat Cliente-Servidor

Implementação de um chat utilizando sockets TCP, permitindo comunicação contínua entre cliente e servidor.

### Funcionalidades

* Envio e recebimento de mensagens
* Comunicação bidirecional
* Encerramento com comando `QUIT`

---

### Como executar (TCP)

No diretório `q2-chat/tcp`:

Terminal 1:

```
python server.py
```

Terminal 2:

```
python client.py
```

---

### Como executar (UDP)

No diretório `q2-chat/udp`:

Terminal 1:

```
python server.py
```

Terminal 2:

```
python client.py
```

---

## Questão 3 – Aplicação

Aplicação desenvolvida utilizando sockets.

### Descrição

A aplicação desenvolvida é um sistema de chat com transferência de arquivos utilizando socket TCP em Python. O servidor aguarda a conexão de um cliente e, após conectado, oferece um menu de comandos. O usuário pode listar os arquivos disponíveis no servidor, baixar um arquivo do servidor para o cliente, enviar um arquivo do cliente para o servidor, e trocar mensagens de chat em tempo real. A comunicação é feita via protocolo TCP na porta 10389, garantindo a entrega confiável dos dados.


---

### Como executar

No diretório `q3- Aplicacao`:

Terminal 1:

```
python q3_servidor.py
```

Terminal 2:

```
python q3-cliente.py
```

---

## Vídeos

* Vídeo 1 (Questões 1 e 2): [Redes de Computadores #LAB3 - Questão 1 e Questão 2](https://youtu.be/gvEsuuqGQzg)
* Vídeo 2 (Questão 3): [Redes de Computadores #LAB3 - Questão 3](https://youtu.be/gvEsuuqGQzg)

---

## Observações

* A porta utilizada segue o padrão solicitado (baseada no TIA)
* Os códigos foram desenvolvidos para fins acadêmicos
* O projeto pode ser executado localmente em múltiplos terminais
* No TCP, é necessário iniciar o servidor antes do cliente para não dar erro
