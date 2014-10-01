#!/usr/bin/python2
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

from networkManager import NetworkManager
import socket;
import thread;
import types;
import zlib;
import DataTypes;
from pprint import pprint

network = NetworkManager('localhost', 25565, 'Thebot', 'password')
network.login()

def getData():
	#try:
		while True:
			try:
				network.buff.addRaw(network.recv(1024))
			except socket.error, v:
				pass
		
			for p in network.dispatch.sendData:
				if network.dispatch.bot.comp:
					if len(p) >= network.dispatch.bot.compThreshold:
						length, pdata = network.writeLengthCompression(p)
						pdata2 = zlib.compress(p)
						pdata2 = length+pdata2
						pdata2 = network.writeLength(pdata2)
						network.send(pdata2)
					else:
						pdata = DataTypes.writeVarInt(0) + p
						pdata = network.writeLength(pdata)
						network.send(pdata)
				else:	
					network.send(network.writeLength(p))
					network.dispatch.sendData.remove(p)
			packet = network.buff.getNextPacket()
			if packet:
				a = hex(packet.readVarInt())
				while len(a) < 4:
					a = "0x0" + a[2:]
				a = a.upper().replace("X", "x")
				getattr(network.dispatch, "Packet"+a)(packet)
				if network.dispatch.bot.comp:
					network.buff.comp = True
					network.buff.compThreshold = network.dispatch.bot.compThreshold
	#except:
	#	network.dispatch.bot.loggedIn = False;
	#	print("\nConnection Terminated");
	#	exit();
	
try:
	thread.start_new_thread(getData, ()); 
except:
	print "Error: unable to start thread"

def getObjectData(data):
	dataObject = {};
	for j in dir(data):
		k = getattr(data, j); 
		if j[0] != "_" and j != "printable":
			if k != types.NoneType and hasattr(k, 'printable') and k.printable == True: 
				k = getObjectData(k);
				dataObject[j] = k;
			elif isinstance(k, list):
				k = [];
				for l in k:
					if l != types.NoneType and hasattr(l, 'printable') and l.printable == True: 
							l = getObjectData(l);
					k.append(l);
			elif isinstance(k, types.MethodType):
				continue
			dataObject[j] = k;

	return dataObject;
		
connected = False;
print("Connecting...");
while True:
	if network.dispatch.bot.loggedIn:
		connected = True;
		a = raw_input("mcBot> ");
		if a[:4] == "stop" or a[:4] == "quit" or a[:4] == "exit":
			print("Shutting down...");
			exit();
		elif a[:7] == "getData":
			print("Data:");
			pprint(getObjectData(network.dispatch.bot));
		elif a[:4] == "move":
			args = a[4:];
			b = args.split(" ");
			b.remove("");
			if len(b) == 4:
				if b[3] == "True":
					b[3] = True;
				else:
					b[3] = False;
				network.packetSend.Packet0x04(float(b[0]), float(b[1]), float(b[2]), b[3]);
			else:
				print("usage: move <x> <y> <z> <onGround>");
		elif a == "":
			pass;
		else:
			print("Invalid command");
	elif connected == True:
		print("Connection Terminated");
		exit();
