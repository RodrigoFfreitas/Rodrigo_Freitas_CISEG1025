import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

clients = []

# Criar socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor à procura em: {HOST}:{PORT}")


def Broadcast(message, clientIncome):
    for client in clients:
        if client != clientIncome:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def dealWithClient(clienteSocket, ipAddress):

    print(f"Cliente conectado: {ipAddress}")

    clients.append(clienteSocket)

    while True:
        try:

            messageBytes = clienteSocket.recv(1024)

            if not messageBytes:
                break

            message = messageBytes.decode('utf-8')

            print(f"📩 {ipAddress}: {message}")

            Broadcast(messageBytes, clienteSocket)

        except:
            break

    print(f"Cliente saiu: {ipAddress}")

    clients.remove(clienteSocket)
    clienteSocket.close()


while True:

    clientSocket, ipAddress = server.accept()

    thread = threading.Thread(
        target=dealWithClient,
        args=(clientSocket, ipAddress)
    )

    thread.start()