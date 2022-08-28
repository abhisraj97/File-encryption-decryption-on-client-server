import socket  #importing socket

SERVER_IP = "127.0.0.1" #Server IP using Loopback for testing
PORT = 9000   #Server Port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket
server.bind((SERVER_IP, PORT))  #Bind TCP Stream connectoin
server.listen(2)

print("Waiting for incoming information")
#connecting to sender
conn,addr =server.accept()

print("Connected with sender: ")
conn1, addr2 = server.accept() #connecting to receiver
print( "Connected with receiver: ")
print()

#opening blank text file where we write the key
keydata = "serverkey"
keyname = open(keydata,'wb')

#receiving key from sender
key_data=conn.recv(1024)
print("key received to server")

#writing key to other file
keyname.write(key_data)

#flushing the buffer to handle overriding
keyname.flush()
keyname.close()

#opening key text file to read
key=open(keydata,'rb')
data=key.read(18181624)


#sending key to receiver for decrypting
conn1.send(data)
print("key send to receiver")

#opening blank text file where we write the data
filename="Data_recevied"
file=open(filename,'wb')

#receiving file from sender
file_data=conn.recv(1818624)

#writing the received file in another file
file.write(file_data)

#flushing the buffer to handle overriding
file.flush()
#closing the file
file.close()

#opening blank text file to read and sending
file2=open(filename,'rb')
file_data=file2.read(18181624)

file2.flush()

#sending files encrypted data to receiver
conn1.send(file_data)

#closing encrypted file
file2.close()
#s.close()
print("file send to receiver")


