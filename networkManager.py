import socket
import zlib
import DataTypes
import time
import packetDispatch

buff = DataTypes.Buffer()

HOST = 'localhost'
PORT = 25565

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(0)
def writeLength(data):
	return DataTypes.writeVarInt(len(data)) + data

def login():
	global sendData
	packet = "\x00"
	packet += DataTypes.writeVarInt(47)
	packet += DataTypes.writeString(HOST)
	packet += DataTypes.writeUnsignedShort(PORT)
	packet += DataTypes.writeVarInt(2)
	packet = writeLength(packet)
	packetDispatch.sendData += packet
	#Next Packet
	packet = '\x00'
	packet += DataTypes.writeString("TheBot")
	packet = writeLength(packet)
	packetDispatch.sendData += packet


login()

while True:
	try:
		buff.addRaw(s.recv(1024))
	except socket.error, v:
		pass
	if packetDispatch.sendData:
		s.send(packetDispatch.sendData)
		packetDispatch.sendData = ""
	packet = buff.getNextPacket()
	if packet:
		a = hex(packet.readVarInt())
		while len(a) < 4:
			a = "0x0" + a[2:]
		a = a.upper().replace("X", "x")
		packetDispatch.pDispatch[a](packet)

