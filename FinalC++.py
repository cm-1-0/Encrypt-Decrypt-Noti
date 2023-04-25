
from cryptography.fernet import Fernet
import sys
import pync


def load_key():
    return open("unlock_key", "rb").read()


def produce_key():
    with open("unlock_key", "wb") as key_file:
        key_file.write(Fernet.generate_key())


def encrypt():
    file_name = input("What file would you like to Encrypt?(Enter File Name): ")
    secure = Fernet(key)
    with open(file_name, "rb") as file:
        original = file.read()
    encrypted = secure.encrypt(original)
    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt():
    file_name = input("What file would you like to Decrypt?(Enter File Name): ")
    secure = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted = file.read()
    decrypted = secure.decrypt(encrypted)
    with open(file_name, "wb") as file:
        file.write(decrypted)


def unlock():
    global a
    password = input("What is the password for this program: ")
    if password == "C++Final":
        a = 1
        print("Evaluating password")
        while a < 4:
            print(str(a) + "...")
            a += 1
        print("Access Granted")
    else:
        print("Incorrect Password. Terminating")
        sys.exit()


def message():
    file_name = input("Name of File: ")

    with open(file_name, "w") as new_file:
        new_file.write(input("Enter the message: "))


def noti(msg):
    pync.notify(str(msg))


print("Welcome to this Program")

q1 = input("Would you like Access?: ")

if q1 == "Yes":
    unlock()

    q3 = input("Do you need to load a key: ")
    if q3 == "Yes":
        produce_key()
        noti("Key has been Produced")

    q4 = input("Would you like to create a file with a message: ")
    if q4 == "Yes":
        message()
        noti("Message has been recorded")
    else:
        key = load_key()
        q2 = input("Would you like to either Encrypt or Decrypt a file: ")

        if q2 == "Encrypt":
            encrypt()
            noti("File has been encrypted")

        elif q2 == "Decrypt":
            decrypt()
            noti("File has been decrypted")
        else:
            print("Program Terminating")
            sys.exit()
else:
    print("Program Terminating")
    sys.exit()
