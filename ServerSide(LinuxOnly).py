#1.0
import socket
import time 
import os

def listen(): #Listener to catch	
	try:
		host = socket.gethostbyname("www.google.com")
		s = socket.create_connection((host, 80), 2)
	except:
		print("NO INTERNET CONNECTIoN")

	####Linux Only code Start
	gw = os.popen("ip -4 route show default").read().split()
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	#####Linux Only code End
	host = socket.gethostname()
	IP = ipaddr


	print(IP)
	PORT = 4443
	host = IP 

	s = socket.socket()
	s.bind((host,PORT))
	s.listen(50)

	print("Server Waiting...")

	while True:
		conn,addr = s.accept()
		print('Got Connection from: ',addr)
		data = conn.recv(1024)
		print("Server Received",repr(data))

		filename = 'TestFile.txt'#Sends configs.db
		f = open(filename,'rb')#Opens file
		l = f.read(1024)
		while l:## send file data
			conn.send(l)
			print('Sent',repr(l))
			l = f.read(1024)
		f.close()
		
		print("Transmission Complete")
		conn.close()

		
		
listen()
'''What needs to be done:
-If port in use, try other ports. 
-Allow for better error prints '''
