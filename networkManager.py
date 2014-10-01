import socket
import zlib
from DataTypes import Buffer
import time
from packetDispatch import PacketDispatch
from PacketSend import PacketSend

class NetworkManager():
	HOST = ''
	PORT = 25565
	buff = ''
	s = ''
	compressionThreshold = -1
	dispatch = ''
	packetSend = []
	printable = True
	receiveSize = 1024
	
	def recv(self, length):
		return self.s.recv(length)

	def send(self, data):
		data.networkFormat(self.compressionThreshold)
		print "sending: " + data.string.encode("hex")
		self.s.send(data.string);

	def readNewData(self):
		try:
			self.buff.addRaw(self.recv(self.receiveSize))
		except socket.error, v:
			pass

	def handleNewPackets(self):
		packet = self.buff.getNextPacket(self.compressionThreshold != -1)
		while packet:
			# handle packet here
			packetId = packet.readVarInt()
			if packetId == 0x03:
				self.dispatch.Packet0x03(packet)
			packet = self.buff.getNextPacket(self.compressionThreshold != -1)

	def sendWaitingPackets(self):
		for packet in self.packetSend:
			self.send(packet)

	def __init__(self, host, port, username, password):
		self.dispatch = PacketDispatch(self)
		self.buff = Buffer()

		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))
		self.s.setblocking(0)
		

	def login(self):
		global sendData
		# Send handshake
		packet = Buffer();
		packet.writeVarInt(0x00);
		packet.writeVarInt(47);
		packet.writeString(self.HOST);
		packet.writeUnsignedShort(self.PORT);
		packet.writeVarInt(2);
		self.send(packet);
		
		# Send login
		packet = Buffer();
		packet.writeVarInt(0x00);
		packet.writeString("TheBot2");
		self.send(packet);
