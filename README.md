# LAB 03 – Sockets TCP e UDP

## Integrantes

* Nome 1
* Nome 2
* Nome 3

---

## Objetivo

* Implementar e analisar comunicação cliente-servidor utilizando **Sockets TCP e UDP**
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

Contém:

* Execução de cliente e servidor TCP e UDP
* Comparação entre os protocolos
* Análise de erros de conexão e portas

---

## Questão 2 – Chat Cliente-Servidor

Implementação de um chat utilizando sockets:

### Funcionalidades

* Envio e recebimento de mensagens
* Encerramento com comando `QUIT`
* Comunicação cliente-servidor

### ▶ Como executar (TCP)

Terminal 1:

```
python server.py
```

Terminal 2:

```
python client.py
```

### ▶ Como executar (UDP)

Mesmo procedimento acima, utilizando os arquivos da pasta `udp`

---

## Questão 3 – Aplicação

Aplicação desenvolvida utilizando sockets.

### Descrição

Descreva aqui brevemente a ideia da aplicação (ex: chat com múltiplos clientes, envio de arquivos, etc.)

### ▶ Como executar

Terminal 1:

```
python server.py
```

Terminal 2:

```
python client.py
```

---

## Vídeos

* Vídeo 1 (Questões 1 e 2): [link aqui]
* Vídeo 2 (Questão 3): [link aqui]

---

## ⚠️ Observações

* A porta utilizada segue o padrão solicitado (TIA)
* Os códigos foram desenvolvidos para fins acadêmicos
* O projeto pode ser executado localmente em múltiplos terminais

---
