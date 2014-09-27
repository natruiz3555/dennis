import socket
import zlib
import DataTypes
import time
from packetDispatch import PacketDispatch
class NetworkManager():
	HOST = ''
	PORT = 25565
	buff = ''
	s = ''
	comp = False
	compThreshold = 0
	dispatch = ''
	
	def recv(self, length):
		return self.s.recv(length)
	def send(self, data):
		self.s.send(data)
	def __init__(self, dispatch, host, port, username, password):
		self.dispatch = dispatch
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
		self.dispatch.sendData.append(packet)
		#Next Packet
		packet = '\x00'
		packet += DataTypes.writeString("TheBot")
		packet = self.writeLength(packet)
		self.dispatch.sendData.append(packet)
dispatch = PacketDispatch()
network = NetworkManager(dispatch, 'localhost', 25565, 'Thebot', 'password')
network.login()

	

while True:
	try:
		network.buff.addRaw(network.recv(1024))
	except socket.error, v:
		pass

	for p in network.dispatch.sendData:
		network.send(p)
		network.dispatch.sendData.remove(p)
	packet = network.buff.getNextPacket()
	if packet:
		a = hex(packet.readVarInt())
		while len(a) < 4:
			a = "0x0" + a[2:]
		a = a.upper().replace("X", "x")
		getattr(network.dispatch, "Packet"+a)(packet)
