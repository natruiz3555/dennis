#
#  Copyright 2014 Nathan Ruiz <natruiz3553@gmail.com>
# 
# McBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from DataTypes import Buffer;

class PacketSend():
	network = None;
	
	def __init__(self, network):
		self.network = network;

	# Handshake
	def Packet0x00_0(self, host, port):
                packet = Buffer();
                packet.writeVarInt(0x00);
                packet.writeVarInt(47);
                packet.writeString(host);
                packet.writeUnsignedShort(port);
                packet.writeVarInt(2);
                self.network.send(packet);
	# Login
	def Packet0x00_1(self, username):
                packet = Buffer();
                packet.writeVarInt(0x00);
                packet.writeString(username);
                self.network.send(packet);

	
	def Packet0x04(self, X, Y, Z, onGround):
		packet = Buffer();
		packet.writeVarInt(0x04);
		packet.writeDouble(float(X));
		packet.writeDouble(float(Y));
		packet.writeDouble(float(Z));
		packet.writeBool(bool(onGround));
		self.network.send(packet);

