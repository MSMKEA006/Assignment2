import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

nickname = input("Enter your nickname: ")
chatID = input("Enter your chatID: ")

try:
    client.connect(('127.0.0.1', 55555))
    
except:
    print("Please check server address and port")
    print("Goodbye...")

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "Nickname?":
                client.send(nickname.encode('ascii'))
                pass
            else:
                print(f'{message}')

        except:
            print("An error occcured!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_Thread = threading.Thread(target=receive)
receive_Thread.start()

write_Thread = threading.Thread(target=write)
write_Thread.start()