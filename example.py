#!/usr/bin/python2
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
	try:
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
	except:
		network.dispatch.bot.loggedIn = False;
		print("\nConnection Terminated");
		exit();
	
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
	if network.dispatch.bot.loggedIn and connected == False:
		connected = True;
		a = raw_input("mcBot> ");
		if a == "stop" or a == "quit" or a == "exit":
			print("Shutting down...");
			exit();
		elif a == "getData":
			print("Data:");
			pprint(getObjectData(network.dispatch.bot));
		else:
			print("Invalid command");
	elif network.dispatch.bot.loggedIn == False and connected == True:
		print("Connection Terminated");
		exit();