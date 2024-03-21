# Uncomment this to pass the first stage
import socket


def main():

#     print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept()  
    print('connected to: ', addr)
    pong = "+PONG\r\n"

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(pong.encode())

    conn.close()

    # with conn:
    #     conn.recv(1024)
    #     conn.send(pong.encode())


if __name__ == "__main__":
    main()
