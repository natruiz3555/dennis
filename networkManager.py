#
#  Copyright 2014 Epsilon232 <2014ryan@student.ncc.vic.edu.au>
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
import thread
import socket
import zlib
from DataTypes import Buffer
import time
from packetDispatch import PacketDispatch
from PacketSend import PacketSend
import os

class NetworkManager():
	
	def __init__(self, host, port, username, password):
		self.dispatch = PacketDispatch(self)
		self.buff = Buffer()
		self.packetSend = [];
		self.sendPacket = PacketSend(self);
		self.printable = True
		self.receiveSize = 1024
		self.compressionThreshold = -1
		self.username = username;

		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))
		self.s.setblocking(1)

	def recv(self, length):
		data = self.s.recv(length)
		if len(data) < length:
			raise Exception("Requested "+str(length)+" bytes but recieved "+str(len(data)))
		return data;

	def send(self, data):
		data.networkFormat(self.compressionThreshold)
		#print("->" + data.string.encode("hex"));
		self.s.send(data.string);

	def readNewData(self):
		self.buff.addRaw(self.recv(self.receiveSize))

	def handleNewPackets(self, source=None):
		packet = self.buff.getNextPacket(self.compressionThreshold, source)
		#while packet:
			# handle packet here
		if isinstance(packet, Buffer) and len(packet.string) > 0:
			packetId = hex(packet.readVarInt());
			while len(packetId) < 4:
				packetId = "0x0" + packetId[2:];
			packetId = packetId.upper().replace("X", "x")
			#print("<-"+packetId+": "+packet.string.encode("hex"));
			getattr(self.dispatch, "Packet"+packetId)(packet);
		#	packet = self.buff.getNextPacket(self.compressionThreshold != -1)

	def sendWaitingPackets(self):
		for packet in self.packetSend:
			self.send(packet)
			self.packetSend.remove(packet);
		#self.packetSend = []
		

	def networkLoop(self):
		while True:
			self.handleNewPackets(self);
			self.sendWaitingPackets();

	def beginUpdatePositions(self):
		while True:
			thread.start_new_thread(self.updatePosition, ());
			time.sleep(0.05);

	# updates location every 50 ms
	def updatePosition(self):
		bot = self.dispatch.bot;
		location = bot.location;
		if location.x != None and location.y != None and location.z != None:
			self.sendPacket.Packet0x04(location.x, location.y, location.z, bot.onGround);
		return True;

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
		packet.writeString(self.username);
		self.send(packet);
		
		# Start main network loop
		thread.start_new_thread(self.networkLoop, ());

		# Start position update loop
		thread.start_new_thread(self.beginUpdatePositions, ());

		self.dispatch.bot.loggedIn = True;
