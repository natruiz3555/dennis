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
	
	def Packet0x04(self, X, Y, Z, onGround):
		packet = Buffer();
		packet.writeVarInt(0x04);
		packet.writeDouble(X);
		packet.writeDouble(Y-1.62);
		packet.writeDouble(Z);
		packet.writeBool(True);
		packet.writeLength()
		self.network.send(packet);
