#
#  Copyright 2014 natruiz3553 <natruiz3553@gmail.com>
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
	comp = False
	compThreshold = 0
	dispatch = ''
	packetSend = None;
	printable = True;
	
	def recv(self, length):
		return self.s.recv(length)
	def send(self, data):
		self.s.send(data.string);
	def __init__(self, host, port, username, password):
		self.dispatch = PacketDispatch(self)
		self.buff = Buffer()

		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))
		self.s.setblocking(0)
		
		self.packetSend = PacketSend(self);
		
	def writeLength(self, data):
		return self.buff.writeVarInt(len(data)) + data
		
	def writeLengthCompression(self, data):
		return self.buff.writeVarInt(len(data)), data

	def login(self):
		global sendData
		# Send handshake
		packet = Buffer();
		packet.writeVarInt(0x00);
		packet.writeVarInt(47);
		packet.writeString(self.HOST);
		packet.writeUnsignedShort(self.PORT);
		packet.writeVarInt(2);
		packet.writeLength();
		self.send(packet);
		
		# Send login
		packet = Buffer();
		packet.writeVarInt(0x00);
		packet.writeString("TheBot2");
		packet.writeLength();
		self.send(packet);
