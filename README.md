# Encriptación

## Instalación de la librería de criptografía

Para instalar la librería de criptografía, corra lo siguiente:

pip install cryptography


## ejecutar el programa (sin comillas en los paths ni clave): 
### python script.py encrypt "path-de-la-imagen"



## Para desencriptar: 
### python script.py decrypt "path-de-la-imagen" --key "tu-clave"


## Notas:

El script verifica si el archivo proporcionado es una imagen válida antes de realizar la encriptación.
La clave de encriptación se genera de manera aleatoria para cada encriptación, lo que mejora la seguridad en comparación con el uso de una clave fija.
El script guarda la imagen encriptada en un nuevo archivo para no sobrescribir la imagen original.
Se manejan posibles errores y se proporcionan mensajes de error informativos en caso de problemas.
AES ofrece seguridad adicional para verificar que los datos no se hayan alterado durante la transferencia o almacenamiento.


# Encriptación de Imágenes
Verifica si el archivo proporcionado es una imagen.
Genera una clave y un vector de inicialización (IV) aleatorios.
Abre el archivo de la imagen y lee sus datos.
Crea un objeto Cipher con el algoritmo AES y el modo CFB utilizando la clave y el IV.
Cifra los datos de la imagen utilizando el encryptor del objeto Cipher.
Guarda el IV al inicio del archivo cifrado y luego los datos cifrados en un nuevo archivo con la extensión ".enc".


# Desencriptación de Imágenes
Lee el archivo cifrado que se desea desencriptar.
Lee los primeros 16 bytes del archivo para obtener el IV.
Crea un objeto Cipher con el algoritmo AES y el modo CFB utilizando la clave de desencriptación proporcionada en formato hexadecimal y el IV.
Descifra los datos del archivo utilizando el decryptor del objeto Cipher.
Determina la extensión original de la imagen.
Guarda la imagen desencriptada en un nuevo archivo con el nombre y la extensión originales.

Básicamente Utiliza el algoritmo AES, que es altamente confiable, y genera claves y Initialization Vectors (IV) aleatorios para cada operación. Además, maneja errores y almacena las claves de desencriptación de forma segura. 

"Advanced Encryption Standard (AES) es uno de los algoritmos de cifrado más utilizados y seguros actualmente disponibles. Es de acceso público, y es el cifrado que la NSA utiliza para asegurar documentos con la clasificación "top secret". Su historia de éxito se inició en 1997, cuando el NIST (Instituto Nacional de Estándares y Tecnología) comenzó oficialmente a buscar un sucesor al envejecimiento cifrado estándar DES. Un algoritmo llamado "Rijndael", desarrollado por los criptografistas belgas Daemen y Rijmen, sobresalía tanto en seguridad como en rendimiento y flexibilidad."

# Referencias:
## https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/ 
## https://www.boxcryptor.com/es/encryption/ 



