import hashlib 

#text = "Hello, world!"
#hash_object = hashlib.sha256(text.encode())
#hash_digest = hash_object.hexdigest()
#print(hash_digest)

def hash_file(file_path):
    h = hashlib.sha256()
    with open(file_path,'rb') as file:
        while True:
            chunk = file.read(8192)
            if chunk == b'':
                break;
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1,file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        print("File is intact")
    else:
        print("File is corrupted")

if __name__ == "__main__":
    print("SHA256 hash of the file is: ", hash_file("samples/sample.txt"))