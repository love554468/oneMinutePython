import hashlib
str = "test string"
a = hashlib.sha512(bytes(str,encoding="ascii")).hexdigest
print(a)