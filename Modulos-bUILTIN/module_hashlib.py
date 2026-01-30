import hashlib

texto = "SENHA2345"

hash_obj = hashlib.sha256(texto.encode())
hash_result = hash_obj.hexdigest() 
print(hash_result)