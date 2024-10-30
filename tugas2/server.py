import socket
from Crypto.Cipher import DES
import base64

# Kunci 8 byte untuk DES
KEY = b'8bytekey'  # Panjang kunci harus 8 byte untuk DES

def decrypt_message(encrypted_message):
    des = DES.new(KEY, DES.MODE_ECB)
    # Decode dari base64 dan dekripsi
    decrypted_message = des.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.rstrip(b'\x00').decode('utf-8')  # Menghilangkan padding

# Setup socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1)

print("Menunggu pesan terenkripsi dari client...")
conn, addr = server_socket.accept()

try:
    encrypted_message = conn.recv(1024).decode('utf-8')
    print("Pesan terenkripsi diterima:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message)
    print("Pesan setelah didekripsi:", decrypted_message)

finally:
    conn.close()
    server_socket.close()
