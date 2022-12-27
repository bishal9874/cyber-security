import rsa

public_key, private_key = rsa.newkeys(1024)
with open("public_key and private key/public.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
with open("public_key and private key/private.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))