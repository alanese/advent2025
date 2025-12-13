import hashlib

def find_zeroes(secret: bytes, count: int):
    i = 0
    while True:
        i += 1
        data = secret + bytes(str(i), 'ascii')
        digest = hashlib.md5(data).hexdigest()
        if digest[:count] == "0"*count:
            return i


with open("input-04.txt", 'rb') as f:
    secret = f.read()

print(find_zeroes(secret, 5))
print(find_zeroes(secret, 6))

#-------
#while True: