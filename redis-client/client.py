import socket


def client():
    host = "127.0.0.1"
    port = 6379

    c = socket.socket()

    c.connect((host, port))

    while True:
        message = input("Input your message: (press 'q' to quit):  ")
        if message == "q":
            break
        c.send(message.encode())

        data = c.recv(1024).decode()

        print("From Server: ", data)

    c.close()


if __name__ == "__main__":
    client()
