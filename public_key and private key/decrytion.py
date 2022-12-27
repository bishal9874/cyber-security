import rsa
with open("public_key and private key/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

decr_mess =  open("public_key and private key/encryted.message", "rb").read()

clear_message = rsa.decrypt(decr_mess,private_key)
print(clear_message.decode())