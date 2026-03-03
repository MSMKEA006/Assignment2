import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Enter your nickname: ")

client.connect(('127.0.0.1', 5555))

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