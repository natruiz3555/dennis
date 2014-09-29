from DataTypes import Buffer;

class PacketSend():
	network = None;
	
	def __init__(self, network):
		self.network = network;
	
	def Packet0x04(self, X, Y, Z, onGround):
		packet = Buffer();
		packet.writeVarInt(0x04);
		packet.writeDouble(X);
		packet.writeDouble(Y-1.62);
		packet.writeDouble(Z);
		packet.writeBool(True);
		packet.writeLength()
		self.network.send(packet);