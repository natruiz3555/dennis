import socket
import zlib
import DataTypes
import time
import packetDispatch
class NetworkManager():
	HOST = ''
	PORT = 25565
	buff = ''
	s = ''
	
	def recv(self, length):
		return self.s.recv(length)
	def send(self, data):
		self.s.send(data)
	def __init__(self, host, port, username, password):
		self.buff = DataTypes.Buffer()

		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))
		self.s.setblocking(0)
		
	def writeLength(self, data):
		return DataTypes.writeVarInt(len(data)) + data

	def login(self):
		global sendData
		packet = "\x00"
		packet += DataTypes.writeVarInt(47)
		packet += DataTypes.writeString(self.HOST)
		packet += DataTypes.writeUnsignedShort(self.PORT)
		packet += DataTypes.writeVarInt(2)
		packet = self.writeLength(packet)
		packetDispatch.sendData += packet
		#Next Packet
		packet = '\x00'
		packet += DataTypes.writeString("TheBot")
		packet = self.writeLength(packet)
		packetDispatch.sendData += packet

network = NetworkManager('localhost', 25565, 'Thebot', 'password')
network.login()

while True:
	try:
		network.buff.addRaw(network.recv(1024))
	except socket.error, v:
		pass
	if packetDispatch.sendData:
		network.send(packetDispatch.sendData)
		packetDispatch.sendData = ""
	packet = network.buff.getNextPacket()
	if packet:
		a = hex(packet.readVarInt())
		while len(a) < 4:
			a = "0x0" + a[2:]
		a = a.upper().replace("X", "x")
		packetDispatch.pDispatch[a](packet)

