from modules.hash import hash_file, verify_integrity
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_strength, hash_pw, verify_password
from getpass import getpass
def menu():
    print("Select operation:")
    print("1. Hash File")
    print("2. Verify Integrity")
    print("3. AES Encryption")
    print("4. RSA Encryption")
    print("5. Password Manager")
    print("6. Exit")
   

print("Welcome to the Security Toolkit")
while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        file_path = input("Enter file path: ")
        print(hash_file(file_path))
    elif choice == "2":
        file1 = input("Enter file1 path: ")
        file2 = input("Enter file2 path: ")
        print(verify_integrity(file1,file2))
    elif choice == "3":
        message = input("Enter message: ").encode()
        key, ciphertext, plaintext = aes_ed(message)
        print("AES Key: ",key)
        print("AES Ciphertext: ",ciphertext)
        print("AES Plaintext: ",plaintext)
    elif choice == "4":
        message = input("Enter message: ").encode()
        ciphertext, plaintext = rsa_ed(message)
        print("RSA message, encrypted with a public key: ",ciphertext)
        print("RSA message, decrypted with a private key: ",plaintext)
    elif choice == "5":
        while True:
            password1 = getpass("Enter password: ")
            print(check_strength(password1))
            if check_strength(password1).startswith("Weak"):
                print("Please enter a stronger password")
            else:
                break
        hashed_password = hash_pw(password1)
        print("Hashed password: ", hashed_password)
        attempt = getpass("Enter password to verify: ")
        print(verify_password(attempt,hashed_password))
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        
print("Thank you for using the Toolkit")