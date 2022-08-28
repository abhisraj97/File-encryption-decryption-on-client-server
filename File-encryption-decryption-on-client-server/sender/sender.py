#Using symmetric key here

import socket  #importing socket
from cryptography.fernet import Fernet    #importing fernet from cryptography

SENDER_IP = "127.0.0.1"    #server IP of 127.0.0.1 LOOPBACK used for testing
PORT = 9000         # server Port

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket creation
sender.connect((SENDER_IP, PORT)) #TCP connection
print("connected to server")
#key generation
key = Fernet.generate_key()

#writing the key in a file
file = open('key.key','wb')
file.write(key) # the key is of type bytes
print("key generated")

#opening the key
file = open('key.key','rb')
file_dat=file.read(1818624)

#sending key to server
sender.send(file_dat)
print("key sended")

file.close()

filename=input(str("Input filename with extension you want to send  : "))

#using the generated key
fernet = Fernet(key)

#opening the original file to encrypt
with open (filename,'rb') as file :
    data = file.read()
    #encrypting the file
    encrypted = fernet.encrypt(data)

  # opening the file in write mode and
  #writing the encrypted file
with open ('file.txt','wb') as file:
      file.write(encrypted)
     
print("file encrypted")     

#opening the encrypted file and
#sending it to server
sendfile=open('file.txt','rb')
send_data=sendfile.read(1818624)

sender.send(send_data)
sendfile.close()
print("file sent")

