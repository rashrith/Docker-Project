#! /usr/bin/python3
import asyncio
from audioop import reverse
import socket 
import os

path = '/home/data'
st=""
total=0
fs = os.listdir(path)
res=""

print("Files in /home/data are : ")
for f in fs:
	res=res+f+'\n'
for f in fs:
    if f.endswith('.txt'):
        fopen=open(path+'/'+f,"r",encoding="utf-8")
        s=(fopen.read().replace("\n"," ")).split()
        total=total+len(s)
        res=res+"Number of words in file "+str(f)+" is: "+str(len(s))+"\n"
        if fopen.name.endswith("IF.txt"):
            st=s
            
z={}
for i in st:
    if i not in z:
         z[i]=1
    else:
        z[i]=z[i]+1


sd= sorted(z.items(), key=lambda x: x[1],reverse=True)

res=res+"Top 3 words and their count:\n"+""+str(sd[0])+'\n'+""+str(sd[1])+'\n'+""+str(sd[2])+'\n'+"Total no of words in both the files : "+str(total)+"\n"+"IP address: "+str(socket.gethostbyname(socket.gethostname())+"\n")

fo=open("/home/output/result.txt","w")
fo.write(res)
fo.close()
fo=open("/home/output/result.txt","r")
print(fo.read()) 
