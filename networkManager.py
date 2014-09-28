import socket
import zlib
import DataTypes
import time
from packetDispatch import PacketDispatch
from PacketSend import PacketSend

class NetworkManager():
	HOST = ''
	PORT = 25565
	buff = ''
	s = ''
	comp = False
	compThreshold = 0
	dispatch = ''
	packetSend = None;
	printable = True;
	
	def recv(self, length):
		return self.s.recv(length)
	def send(self, data):
		self.s.send(data)
	def __init__(self, host, port, username, password):
		self.dispatch = PacketDispatch()
		self.buff = DataTypes.Buffer()

		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))
		self.s.setblocking(0)
		
		self.packetSend = PacketSend(self.dispatch);
		
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
	