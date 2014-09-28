import DataTypes

class PacketSend():
	dispatch = None;
	
	def __init__(self, dispatch):
		self.dispatch = dispatch;
	
	def Packet0x04(self, X, Y, Z, onGround):
		packet = "\x04"
		packet += DataTypes.writeDouble(X);
		packet += DataTypes.writeDouble(Y-1.62);
		packet += DataTypes.writeDouble(Z);
		packet += DataTypes.writeBool(True);
		packet = self.writeLength(packet)
		self.dispatch.sendData.append(packet)