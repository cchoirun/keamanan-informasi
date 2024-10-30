import socket
from Crypto.Cipher import DES
import base64

# Kunci 8 byte untuk DES
KEY = b'8bytekey'  # Panjang kunci harus 8 byte untuk DES

def encrypt_message(message):
    des = DES.new(KEY, DES.MODE_ECB)
    # Padding agar panjangnya kelipatan 8
    padded_message = message.ljust((len(message) + 7) // 8 * 8, '\x00')
    encrypted_message = des.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(encrypted_message).decode('utf-8')  # Encode ke base64

# Setup socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))

try:
    message = input("Masukkan pesan yang akan dienkripsi dan dikirim: ")
    encrypted_message = encrypt_message(message)
    print("Pesan terenkripsi:", encrypted_message)

    client_socket.sendall(encrypted_message.encode('utf-8'))

finally:
    client_socket.close()
