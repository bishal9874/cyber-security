
# Example Python program that creates message digests
# using MD5, SHA-256, SHA-512 and BLAKE2b hash functions
import hashlib

msg = b"Hello world"
print("Message:%s"%msg)

# Create an MD5 hash
md5Object = hashlib.md5()
md5Object.update(msg)
md5Digest = md5Object.hexdigest()
print("MD5 hash:")
print(md5Digest)

# Create an SHA-256 hash
sha256Object = hashlib.sha256()
sha256Object.update(msg)
digest_sha256 = sha256Object.hexdigest()
print("Sha-256 hash:")
print(digest_sha256)

# Create an SHA-512 hash
sha512Object = hashlib.sha512()
sha512Object.update(msg)
digest_sha512 = sha512Object.hexdigest()
print("Sha-512 hash:")
print(digest_sha512)

# Create a Blake2b hash
blake2bObject = hashlib.blake2b()
blake2bObject.update(msg)
digest_blake2b = blake2bObject.hexdigest()
print("Blake2b hash:")
print(digest_blake2b)