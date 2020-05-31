import sys
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove, path
from enigma import Enigma


def process_file(file_path: str, enigma_instance, encrypt: bool):
    # Create temp file
    fd, abs_path = mkstemp()

    with fdopen(fd, 'w') as new_file:
        with open(file_path) as old_file:
            if encrypt:
                new_file.write(enigma_instance.encrypt_text(old_file.read()))
            else:
                new_file.write(enigma_instance.decrypt_text(old_file.read()))

    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def run():
    _, action, file_path = sys.argv

    action = action.strip().lower()

    if action == "encrypt":
        key = input("   Enter a key: ")

    elif action == "decrypt":
        key = input("   Enter the decryption key: ")

    else:
        print("Must pass either 'encrypt' or 'decrypt' as the second argument.")
        exit()

    if path.exists(file_path):
        enigma = Enigma(key)
        encrypt = action == "encrypt"
        process_file(file_path, enigma, encrypt)

    else:
        print('Please enter a valid file path')


if __name__ == "__main__":
    run()
