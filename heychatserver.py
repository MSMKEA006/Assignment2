import threading
import socket
import database
from message import Message

host = "127.0.0.1" # localHost address
port = 55555 # higher number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

database.createDB()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            print("***Error occured***")

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
            nicknames.remove(nickname)

            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send(f"Nickname?".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        print(f'Nickname of the client is {nickname}!')
        

        
        nicknames.append(nickname)
        clients.append(client)

        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()