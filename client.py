import socket
import time

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9000))

message = ''
received_data = ''
while message != 'see ya' or received_data != 'see ya':
    expected_data_size = int(sock.recv(4).decode())

    received_data = ''
    while len(received_data) < expected_data_size:
        # Ler o dado recebido
        received_data += sock.recv(4).decode()

    print(received_data)
    if received_data == 'see ya':
        break

    message = raw_input("Digite sua mensagem: ").strip()
    send_data_size = len(message)
    sock.sendall(str(send_data_size).zfill(4).encode())

    # Enviar a mensagem
    sock.sendall(message.encode())

# Finalizar a conexao
sock.close()
