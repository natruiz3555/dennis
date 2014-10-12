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
from Location import Location
from packetDispatch import PacketDispatch
from PacketSend import PacketSend
import os

class NetworkManager():
	
	def __init__(self, host, port, username, password):
		self.origin = Location();
		self.origin.set(130, 71, 83);
		self.range = Location();
		self.range.set(10,10,10);
		self.X = 0;
		self.Y = 0;
		self.Z = 0;
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
		self.s.settimeout(None);
		try:
			self.s.connect((self.HOST, self.PORT))
		except socket.error:
			print("Connection refused");
			thread.interrupt_main();
			exit();

	def recv(self, length):
		data = "";
		while length > self.receiveSize:
			data += self.s.recv(self.receiveSize);
			length -= self.receiveSize;
		data += self.s.recv(length);
		if len(data) < length:
			# because the socket is blocking, this would indicate a dead connection
			raise Exception("Requested "+str(length)+" bytes but recieved "+str(len(data)))
			thread.interrupt_main();
			exit();
		return data;

	def send(self, data):
		data.networkFormat(self.compressionThreshold)
		#print("->" + data.string.encode("hex"));
		try:
			self.s.send(data.string);
		except socket.error:
			print("Connection terminated.");
			thread.interrupt_main();
			exit();

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
			try:
				thread.start_new_thread(self.updatePosition, ());
			except KeyboardInterrupt:
				self.s.close();
				thread.interrupt_main();
				exit();
			time.sleep(0.05);

	# updates location every 50 ms
	def updatePosition(self):
		bot = self.dispatch.bot;
		location = bot.location;
		if bot.location.x != None:
			bot.location.x += self.X;
		if bot.location.y != None:
			bot.location.y += self.Y;
		if bot.location.z != None:
			bot.location.z += self.Z;
			
		if location.x != None and location.y != None and location.z != None:
			self.sendPacket.Packet0x04(location.x, location.y, location.z, bot.onGround);
		return True;

	def login(self):
		# Send handshake
		self.sendPacket.Packet0x00_0(self.HOST, self.PORT);
		
		# Send login
		self.sendPacket.Packet0x00_1(self.username);
		
		# Start main network loop
		try:
			thread.start_new_thread(self.networkLoop, ());
		except KeyboardInterrupt:
			self.s.close();
			print("interupt 1");
			exit();

		# Start position update loop
		try:
			thread.start_new_thread(self.beginUpdatePositions, ());
		except KeyboardInterrupt:
			self.s.close();
			print("interupt 2");
			exit();

		self.dispatch.bot.loggedIn = True;
