
import socket #importing socket
from cryptography.fernet import Fernet   #importing fernet from cryptography

RECEIVER_IP = "127.0.0.1"    # The remote host
PORT = 9000             # The same port as used by the server


receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #TCP socket creation
receiver.connect((RECEIVER_IP, PORT))   #TCP connection




#file for accepting key from server
keydata = "receiver's key"

#opening the text file as keyname where we write the key
keyname = open(keydata,'wb')

#receiving key from server
key_data=receiver.recv(1024)

#writing key to other file
keyname.write(key_data)

#After receiving key from server flushing the buffer to handle overriding
keyname.flush()
keyname.close()
print("key received to receiver")

#opening the file as filekey which contains key
with open (keydata,'rb') as filekey:
    key = filekey.read()

#using the received key from server
fernet = Fernet(key)

#Taking a file for receiving data 
filename="Encrypted Data"
file=open(filename,'wb')

#receiving encrypted file from server
file_data=receiver.recv(1818624)
file.write(file_data)

#After receiving key flushing the buffer to handle overriding
file.flush()
print("file received")


#using received key from server
fernet = Fernet(key)

#opening received encrypted file as enc_file
with open (filename,'rb') as enc_file:
    encrypted = enc_file.read()
    
#decrypting the encrypted file
decrypted = fernet.decrypt(encrypted)

#Taking input filename in which we put the the decryptrd file
filenamem=input(str("Please Enter a file name with extension to receive the incoming file : "))


with open (filenamem,'wb') as dec_file:
    dec_file.write(decrypted)
      
print("file decrypted")


receiver.close()


print("Goodbye..")
print()