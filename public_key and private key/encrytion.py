import rsa


with open("public_key and private key/public.pem","rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())
with open("public_key and private key/private.pem","rb") as f:
     private_key =rsa.PrivateKey.load_pkcs1(f.read())

message = input("enter the Message: ")
encrypted_message = rsa.encrypt(message.encode(),public_key)
print(encrypted_message)
with open("public_key and private key/encryted.message","wb") as f:
    f.write(encrypted_message)