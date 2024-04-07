import hashlib
import os

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_integrity(file_path, expected_checksum):
    actual_checksum = calculate_sha256(file_path)
    return actual_checksum == expected_checksum

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    expected_checksum = input("Enter the expected SHA-256 checksum: ")

    if os.path.isfile(file_path):
        if check_integrity(file_path, expected_checksum):
            print("File integrity verified: The file has not been tampered with.")
        else:
            print("File integrity check failed: The file may have been tampered with.")
    else:
        print("Error: File not found.")
