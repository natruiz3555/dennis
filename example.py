#!/usr/bin/python2
from networkManager import NetworkManager
import socket;
import thread;
import types;
from pprint import pprint

network = NetworkManager('localhost', 25565, 'Thebot', 'password')
network.login()

	
def getData():
	while True:
		try:
			network.buff.addRaw(network.recv(1024))
		except socket.error, v:
			pass
	
		for p in network.dispatch.sendData:
			network.send(p)
			network.dispatch.sendData.remove(p)
		packet = network.buff.getNextPacket()
		if packet:
			a = hex(packet.readVarInt())
			while len(a) < 4:
				a = "0x0" + a[2:]
			a = a.upper().replace("X", "x")
			getattr(network.dispatch, "Packet"+a)(packet)

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
		

while True:
	a = raw_input("mcBot> ");
	if a == "stop" or a == "quit" or a == "exit":
		print("Shutting down...");
		exit();
	elif a == "getData":
		print("Data:");
		pprint(getObjectData(network.dispatch.bot));
	else:
		print("Invalid command");