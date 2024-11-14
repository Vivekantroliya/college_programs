'''
Q.9 Implement a stand-alone sender receiver
program in which Sender encrypts a given text
message entered from keyboard using RSA
public key of Receiver and sends it to Receiver.
Receiver Decrypts the cipher-text using his own
RSA Private key and display the decrypted
contents on screen. Use Appropriate
package/Library for RSA.
'''
#pip install cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes  # Add this import
import os

def sender():
    # Generate a random plaintext message
    plaintext = input("Enter the message: ").encode()

    # Load the receiver's public key
    with open('receiver_public.pem', 'rb') as f:
        receiver_public_key = serialization.load_pem_public_key(f.read())

    # Encrypt the message using RSA public key with OAEP padding
    ciphertext = receiver_public_key.encrypt(
        plaintext,
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),  # Corrected import
            algorithm=hashes.SHA256(),  # Corrected import
            label=None
        )
    )

    with open('encrypted_message.bin', 'wb') as f:
        f.write(ciphertext)
    print("Message encrypted and saved as 'encrypted_message.bin'")

if __name__ == "__main__":
    sender()
