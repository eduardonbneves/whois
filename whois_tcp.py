#!/usr/bin/python
import socket, sys

if len(sys.argv) < 2:
	print "Usage: " + sys.argv[0] + " example.com"
	exit()

host = sys.argv[1]
dst_port = 43
register = ''

if(host.endswith(".org")):

	register = "199.15.84.131"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((register, dst_port))

	s.send("%s\n" % host)

	print("\nat whois.namecheap.com\n")

	data = ''
	buf = 'a'
	while buf != '':
		buf = s.recv(1024)
		data += buf
	s.close()

	print data

	print '----------------------------------------------------------------\n'


	list = [[data]]
	for index, item in enumerate(list):
		list[index] = item[0].split()

	for s in range(len(list)):
		register = format(list[s][10])

	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s1.connect((socket.gethostbyname(register), dst_port))

	s1.send("%s\n" % host)

	print("at %s\n" % register)

	data = ''
	buf = 'a'
	while buf != '':
		buf = s1.recv(1024)
		data += buf
	s1.close()
	print data
	

elif(host.endswith(".gov")):

	register = "69.58.188.30"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((register, dst_port))

	s.send("%s\n" % host)

	print("\nat internic.net\n")

	data = ''
	buf = 'a'
	while buf != '':
		buf = s.recv(1024)
		data += buf
	s.close()

	print data


elif(host.endswith(".br")) :

	register = "200.160.2.3"
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((register, dst_port))

	s.send("%s\n" % host)

	print("\nat registro.br\n")

	data = ''
	buf = 'a'
	while buf != '':
		buf = s.recv(1024)
		data += buf
	s.close()

	print data.decode("latin-1")

else:

	register = "192.34.234.30"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((register, dst_port))

	s.send("%s\n" % host)

	print("\nat whois.verisign-grs.com\n")

	data = ''
	buf = 'a'
	while buf != '':
		buf = s.recv(1024)
		data += buf
	s.close()
	print data

	print '----------------------------------------------------------------\n'


	list = [[data]]
	for index, item in enumerate(list):
		list[index] = item[0].split()

	for s in range(len(list)):
		register = format(list[s][10])

	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s1.connect((socket.gethostbyname(register), dst_port))

	s1.send("%s\n" % host)

	print("at %s\n" % register)

	data = ''
	buf = 'a'
	while buf != '':
		buf = s1.recv(1024)
		data += buf
	s1.close()
	print data
