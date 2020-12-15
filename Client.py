import socket
import threading 

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",555555))

def recive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "Nick":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        
def 