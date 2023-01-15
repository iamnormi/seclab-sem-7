import hashlib
s=input("Enter the message to encrypt: ")
result=hashlib.sha1(s.encode())
print("The SHA1 for",'`',s,'`',"is..: ",result.hexdigest())
