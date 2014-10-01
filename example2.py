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

while True:
	network.readNewData()
	network.handleNewPackets()
	network.sendWaitingPackets()