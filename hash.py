import hashlib

data = "40817810726200008990_ABEJWA"

#hash_object = hashlib.sha256(data.encode())
hash_object = hashlib.md5(data.encode())

hash_hex = hash_object.hexdigest()

#40817810726200008990 3d6f960118e6a1ffdf67320665c94625
#40817810301200076171

if __name__ == '__main__':
    print(hash_hex)
