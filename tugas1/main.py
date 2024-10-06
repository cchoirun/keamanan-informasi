# Kode ini digunakan untuk menjalankan enkripsi dan dekripsi


from des import des_encrypt, des_decrypt

def main():
    # Contoh input data
    plaintext = [0, 1, 0, 1, 1, 0, 1, 0] * 8  # 64-bit
    key = [1, 0, 1, 0, 0, 1, 1, 1] * 8  # 64-bit

    print("Plaintext:", plaintext)

    # Enkripsi
    ciphertext = des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    # Dekripsi
    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)

    if decrypted_text == plaintext:
        print("Dekripsi berhasil!")
    else:
        print("Dekripsi gagal!")

if __name__ == "__main__":
    main()
