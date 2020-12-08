import threading
import socket

host = "127.0.0.1" #localhost
port = 555555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast (message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode("ascii"))
            nicknames.remove(nickname)
            break

def recive():
    while  True:
        client, address = server.accept()
        print(f"Connectede with {str(address)}")

        client.send("Nick".encode("ASCII"))
        nickname = client.recv(1024).encode("ascii")
        nicknames.append(nickname)
        clients.append(clients)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat !".encode("ascii"))
        client.send("Conected to the server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is listening... ")
recive()