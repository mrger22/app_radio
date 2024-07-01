import hashlib

data = "408178_A"

#hash_object = hashlib.sha256(data.encode())
hash_object = hashlib.md5(data.encode())

hash_hex = hash_object.hexdigest()

if __name__ == '__main__':
    print(hash_hex)
