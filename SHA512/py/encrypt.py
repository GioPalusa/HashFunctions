import hashlib

def encrypt(initial):
  initial = initial.encode('utf-8')
  output = hashlib.sha512(initial.encode())
  return output.hexdigest()
