import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"🟡 A conectar a {HOST}:{PORT}...")
cliente.connect((HOST, PORT))

print("🟢 Conectado ao servidor! (digita 'sair' para encerrar)")


def receber_mensagens():

    while True:

        try:
            mensagem = cliente.recv(1024).decode('utf-8')

            if not mensagem:
                break

            print(f"\n💬 {mensagem}")

        except:
            print("🔴 Conexão perdida.")
            break


thread_receber = threading.Thread(target=receber_mensagens)
thread_receber.start()


while True:

    mensagem = input("Tu: ")

    if mensagem.lower() == "sair":
        break

    cliente.send(mensagem.encode('utf-8'))


cliente.close()
print("🔴 Cliente encerrado.")