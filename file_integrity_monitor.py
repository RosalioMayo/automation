import hashlib
import os

def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

if __name__ == "__main__":
    file_path = input("Enter the file path to monitor: ")
    initial_hash = hash_file(file_path)
    print(f"Initial hash: {initial_hash}")

    input("Press Enter to check the file integrity again...")
    current_hash = hash_file(file_path)
    print(f"Current hash: {current_hash}")

    if initial_hash == current_hash:
        print("File integrity verified.")
    else:
        print("File integrity compromised!")
