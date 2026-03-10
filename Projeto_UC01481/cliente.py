import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"A conectar a {HOST}:{PORT}...")
client.connect((HOST, PORT))

print("Conectado ao servidor! ( Para sair escreva 'sair')")


def ReceberMensagens():

    while True:

        try:
            message = client.recv(1024).decode('utf-8')

            if not message:
                break

            print(f"\n💬 {message}")

        except:
            print("🔴 Conexão perdida!!")
            break


reciveThread = threading.Thread(target=ReceberMensagens)
reciveThread.start()


while True:

    message = input()

    if message.lower() == "sair":
        break

    client.send(message.encode('utf-8'))


client.close()
print("A Fechar o Cliente!")