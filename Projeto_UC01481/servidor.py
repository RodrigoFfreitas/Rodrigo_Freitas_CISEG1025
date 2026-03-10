import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

clientes = []

# Criar socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"🟢 Servidor à escuta em {HOST}:{PORT}...")


def enviar_para_todos(mensagem, cliente_origem):
    for cliente in clientes:
        if cliente != cliente_origem:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)


def lidar_com_cliente(cliente_socket, endereco):

    print(f"🔵 Cliente conectado: {endereco}")

    clientes.append(cliente_socket)

    while True:
        try:

            mensagem_bytes = cliente_socket.recv(1024)

            if not mensagem_bytes:
                break

            mensagem = mensagem_bytes.decode('utf-8')

            print(f"📩 {endereco}: {mensagem}")

            enviar_para_todos(mensagem_bytes, cliente_socket)

        except:
            break

    print(f"🔴 Cliente saiu: {endereco}")

    clientes.remove(cliente_socket)
    cliente_socket.close()


while True:

    cliente_socket, endereco = servidor.accept()

    thread = threading.Thread(
        target=lidar_com_cliente,
        args=(cliente_socket, endereco)
    )

    thread.start()