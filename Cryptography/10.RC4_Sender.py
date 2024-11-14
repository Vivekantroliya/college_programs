'''
Q.10  Implement a stand-alone sender receiver
program in which Sender encrypts a given text
message entered from keyboard in a byte-by-
byte manner using RC4 Stream Cipher and
transmits it to receiver. Receiver Decrypts the
ciphertext displays the decrypted contents on
screen. Use Appropriate package/Library for
RC4.
'''
#pip install cryptography
from Crypto.Cipher import ARC4

def sender():
    # Get the plaintext message from the user
    plaintext = input("Enter the message: ").encode()

    # Enter a shared secret key (password) for encryption
    key = input("Enter a secret key (password): ").encode()

    # Create an RC4 cipher with the provided key
    cipher = ARC4.new(key)

    # Encrypt the message byte-by-byte
    ciphertext = cipher.encrypt(plaintext)

    # Save the encrypted message to a file or transmit it to the receiver
    with open('encrypted_message.bin', 'wb') as f:
        f.write(ciphertext)

    print("Message encrypted and saved as 'encrypted_message.bin'")

if __name__ == "__main__":
    sender()
