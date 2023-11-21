import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_image(file_path):
    # Verificar si el archivo es una imagen o nelson
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        raise ValueError("El archivo proporcionado no es una imagen")

    # Generar clave y IV SIUUUUUUUUUU
    key = os.urandom(32) 
    iv = os.urandom(16)   

    try:

        with open(file_path, 'rb') as fin:
            image_data = fin.read()

        # Cifrar la imagen usando AEs (GOD)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        encrypted_image = encryptor.update(image_data) + encryptor.finalize()

        # Guardar la imagen cifrada en un nuevo arc
        encrypted_path = file_path + ".enc"
        with open(encrypted_path, 'wb') as fout:
            fout.write(iv)  # Guardar IV al inicio del archivo papu
            fout.write(encrypted_image)

        print('Encriptación completada. Archivo encriptado:', encrypted_path)
        print('Clave de encriptación:', key.hex())
    except Exception as e:
        print('Error:', str(e))

# Uso del script
# encrypt_image("ruta/a/tu/imagen.jpg")

def decrypt_image(encrypted_file_path, key):
    try:
        # Leer los datos encriptados de la img
        with open(encrypted_file_path, 'rb') as fin:
            iv = fin.read(16)  # Leer los primeros 16 bytes para el IV que se generó alla arriba dx
            encrypted_data = fin.read()

        # Descifrar la imagen siuuu 
        cipher = Cipher(algorithms.AES(bytes.fromhex(key)), modes.CFB(iv))
        decryptor = cipher.decryptor()
        decrypted_image = decryptor.update(encrypted_data) + decryptor.finalize()


        original_extension = encrypted_file_path.split('.')[-2].split('/')[-1]
        # verif la exntesion de la img
        if original_extension not in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
            raise ValueError("La extensión del archivo original no es un formato de imagen reconocido")

        # Guardar la imagen desencriptada siuuu
        decrypted_path = encrypted_file_path.replace('.enc', f'_decrypted.{original_extension}')
        with open(decrypted_path, 'wb') as fout:
            fout.write(decrypted_image)

        print('Desencriptación completada. Archivo desencriptado:', decrypted_path)
    except Exception as e:
        print('Error:', str(e))


# Uso del script
# decrypt_image("ruta/al/archivo/encriptado.enc", "tu_clave_en_hexadecimal")

def main():
    parser = argparse.ArgumentParser(description="Encriptar y desencriptar imágenes usando AES")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="acción a realizar: 'encrypt' o 'decrypt'")
    parser.add_argument("file_path", help="ruta al archivo a procesar")
    parser.add_argument("--key", help="clave de encriptación para desencriptar, en formato hexadecimal", default="")

    args = parser.parse_args()

    if args.action == "encrypt":
        encrypt_image(args.file_path)
    elif args.action == "decrypt":
        if not args.key:
            raise ValueError("Se requiere una clave para desencriptar")
        decrypt_image(args.file_path, args.key)

if __name__ == "__main__":
    main()



#guia de uso 
#instalar libreria de criptografia: pip install cryptography
#ejecutar el programa: python gfgimproved.py o python3 gfgimproved.py según corresponda.

# ¿Por qué este código es más chidote que el anterior (partiendo de la base del gfg)?
# 1. AES es como un guardia de seguridad mas chidori en comparación con el XOR, que sería un candado básico. AES es bastante seguro.
# 2. Las claves que usamos aquí son generadas al azar, lo cual es mucho mejor que usar una clave fija como "GeeksforGeeks". practicamente Es como tener una contraseña única para cada candado.
# 3. Este código guarda la imagen cifrada en un nuevo archivo en vez de sobrescribir el original pa no perder la foto original
# 4. manejamos los posibles errors.
# 5. Aunque no lo implementamos compleztamente aquí, AES nos permite agregar más seguridad para chequear que nuestros datos no se hayan alterado.
# 6. Usar AES es estar basado en seguridad (creo). 

# En resumen, este código es más seguro y confiable para encriptar nuestras imágenes partiendo de la misma base.

#JESUS DANIEL MARTÍNEZ GARCÍA A00833591

# Referencias: Geeks for geeks encrypt and decrypt an image
#https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/

#https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/ 
