#row & Column
import math

def row(s,key):
    temp=[]
    for i in key:
        if i not in temp:
            temp.append(i)
    k=""
    for i in temp:
        k+=i
    print("The key used for encryption is: ",k)
    b=math.ceil(len(s)/len(k))
    if(b<len(k)):
        b=b+(len(k)-b)

    arr=[['_' for i in range(len(k))]
         for j in range(b)]
    i=0
    j=0
    for h in range(len(s)):
        arr[i][j]=s[h]
        j+=1
        if(j>len(k)-1):
            j=0
            i+=1
    print("The message matrix is: ")
    for i in arr:
        print(i)
    cipher_text=""
    kk=sorted(k)
    for i in kk:
        h=k.index(i)
        for j in range(len(arr)):
            cipher_text+=arr[j][h]
    print("The cipher text is: ",cipher_text)

msg=input("Enter the message: ")
key=input("Enter the key in alphabets: ")
row(msg,key)

###Decryption

import math

def row(s,key):
    temp=[]
    for i in key:
        if i not in temp:
            temp.append(i)
    k=""
    for i in temp:
        k+=i
    print("The key used for encryption is: ",k)

    arr=[['' for i in range(len(k))]
         for j in range(int(len(s)/len(k)))]
    kk=sorted(k)
    d=0
    for i in kk:
        h=k.index(i)
        for j in range(len(k)):
            arr[j][h]=s[d]
            d+=1
    print("The message matrix is: ")
    for i in arr:
        print(i)
    plain_text=""
    for i in arr:
        for j in i:
            plain_text+=j
    print("The plain text is: ",plain_text)


msg=input("Enter the message to be decrypted: ")
key=input("Enter the key in alphabets: ")
row(msg,key)
