#1.0
import socket
import time


def RequestDB(IP):
# send data to another machine
	# test internet connection

	
	try:
		host = socket.gethostbyname("www.google.com")
		s = socket.create_connection((host, 80), 2)
	except:
		print("NO INTERNET CONNECTION")

	# send data
	x = 1
	while x == 1:
		try:
			s = socket.socket()            # Create a socket object
			host = IP    
			PORT = 4443                    # Reserve a port for your service.
			BUFFER_SIZE = 1024

			s.connect((host, PORT))
			s.send(("Connection Test").encode())

			with open('TestFile_.txt', 'wb') as f: #Creates file configs.db
				print('file opened')
				while True:#Start reciving data from server
					print('receiving data...')
					data = s.recv(1024)
					print((data))
					if not data:#Break when all data is sent 
						break
					f.write(data)#write data recived to newly created file
					print(f)

			x = 0 
		except:
			print("Attempt Reconnect")
	s.close()
RequestDB("192.168.0.44")#Change this to your own IP 

'''What needs to be done:
-If port in use, try other ports. 
-Allow for better error prints '''