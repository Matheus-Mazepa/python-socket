import socket
# from socket import *

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escutar a porta 9000
server = sock.bind(('localhost', 9000))

# Definir o limite de 1 conexao paralela
sock.listen(1)

# Aceitar uma conexao e finaliza-la
message = ''
received_data = ''
print("Aguardando conexao")
connection, address_client = sock.accept()

while message != 'see ya' or received_data != 'see ya':
    # Aguardar uma conexao

    message = raw_input("Digite sua mensagem: ").strip()
    tamanho_da_mensagem = len(message)

    # Envio tamanho da mensagem
    connection.sendall(str(tamanho_da_mensagem).zfill(4).encode())
    
    # Enviar mensagem
    connection.sendall(message.encode())
    if message == 'see ya':
        break
    # Aguardar tamanho da mensagem
    expected_data_size = ''
    while(expected_data_size == ''):
        expected_data_size += connection.recv(4).decode()
    expected_data_size = int(expected_data_size)

    while len(received_data) < expected_data_size:
        received_data += connection.recv(4).decode()
    print(received_data)
    if received_data == 'see ya':
        break

    # Finalizar a conexao
connection.close()
sock.close()
