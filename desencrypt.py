from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

try:
    encrypted_path = "11.jpg.enc"

    # Usa la clave y el IV que proporcionaste
    key = b'\xbf\x8ej\xbc\xde\xa7\n\x84\xe2\xef\x99\xfb\xbe\x96m\x8d=\xbe4\xe9\xedB\x00ZS\x12e\xe41x\xadx'
    iv = b'\x180\xf1\xf8\xc5N\xb9V\xc2\x85\x03\x12\xbf%\xfe\x9d'

    # Leer los datos de la imagen cifrada
    with open(encrypted_path, 'rb') as fin:
        # ahí arriba puede reemplazar el iv y key
        encrypted_data = fin.read()

    # Descifrar la imagen
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_image = decryptor.update(encrypted_data) + decryptor.finalize()

    # Guardar la imagen descifrada en un nuevo archivo
    decrypted_path = "decrypted_" + encrypted_path
    with open(decrypted_path, 'wb') as fout:
        fout.write(decrypted_image)

    print('Decryption Done. Decrypted file:', decrypted_path)

except Exception as e:
    print('Error caught:', str(e))
