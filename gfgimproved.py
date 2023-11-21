from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

try:
    # Ruta del archivo de imagen
    path = "01.png"

    # Clave de cifrado generada de manera segura
    key = os.urandom(32)  # Clave AES de 256 bits (basada)

    # Imprimir la ruta del archivo y la clave de cifrado
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # Leer los datos de la imagen
    with open(path, 'rb') as fin:
        image_data = fin.read()

    # Cifrar la imagen usando AES
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_image = encryptor.update(image_data) + encryptor.finalize()

    # Guardar la imagen cifrada en un nuevo archivo
    encrypted_path = path + ".enc"
    with open(encrypted_path, 'wb') as fout:
        fout.write(encrypted_image)

    print('Encryption Done. Encrypted file:', encrypted_path)

except Exception as e:
    print('Error caught:', str(e))


#guia de uso 
#instalar libreria de criptografia: pip install cryptography
#ejecutar el programa: python gfgimproved.py o python3 gfgimproved.py según corresponda.

# ¿Por qué este código es más chidote que el anterior (partiendo de la base del gfg)?
# 1. AES es como un guardia de seguridad de nivel ninja en comparación con el XOR, que sería un candado básico. AES es bastante seguro.
# 2. Las claves que usamos aquí son generadas al azar, lo cual es mucho mejor que usar una clave fija como "GeeksforGeeks". practicamente Es como tener una contraseña única para cada candado.
# 3. Este código guarda la imagen cifrada en un nuevo archivo en vez de sobrescribir el original pa no perder la foto original
# 4. manejamos los posibles errors.
# 5. Aunque no lo implementamos completamente aquí, AES nos permite agregar más seguridad para chequear que nuestros datos no se hayan alterado.
# 6. Usar AES es estar basado en seguridad (creo). 

# En resumen, este código es más seguro y confiable para encriptar nuestras imágenes.

#JESUS DANIEL MARTÍNEZ GARCÍA A00833591

# Referencias: Geeks for geeks encrypt and decrypt an image
#https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/