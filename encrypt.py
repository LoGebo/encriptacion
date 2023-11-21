try:
    # Ruta del archivo de imagen
    path = "01.png" #aquí ponga el path de su imagen profe, saludos

    # Clave de cifrado como texto
    key = "GeeksforGeeks"  #aquí solo le cambie al código de geek for geeks para strings.

    # Imprimir la ruta del archivo y la clave de cifrado
    print('The path of file : ', path)
    print('Key for encryption : ', key)


    fin = open(path, 'rb')

    # Almacenar datos de la imagen
    image = fin.read()
    fin.close()

    # Convertir la imagen en un array de bytes
    image = bytearray(image)

    # Convertir la clave en un array de bytes
    key_bytes = bytearray(key, 'utf-8')

    # Realizar la operación XOR en cada byte
    for index, value in enumerate(image):
        image[index] = value ^ key_bytes[index % len(key_bytes)]

    # Abrir archivo para escribir
    fin = open(path, 'wb')

    # Escribir datos cifrados en la imagen
    fin.write(image)
    fin.close()
    print('Encryption Done...')

except Exception as e:
    print('Error caught : ', str(e))


#cabe destacar que no son las mejores practicas de cifrado actualmente pero es un recurso util para encriptar la imagen.


# Referencias: Geeks for geeks encrypt and decrypt an image
#https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/