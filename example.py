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

from Dennis import Dennis;
import socket;
import time;
import thread;
import types;
import zlib;
import DataTypes;
from pprint import pprint

dennis = Dennis("localhost", 25565, 'Dennis', 'password');
dennis.login();

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



connected = False;
print("Connecting...");
#while True:
#	if network.dispatch.bot.loggedIn:
#		connected = True;
#		a = raw_input("mcBot> ");
#		if a[:4] == "stop" or a[:4] == "quit" or a[:4] == "exit":
#			print("Shutting down...");
#			exit();
#		elif a[:7] == "getData":
#			print("Data:");
#			pprint(getObjectData(network.dispatch.bot));
#		elif a[:4] == "move":
#			args = a[4:];
#			b = args.split(" ");
#			b.remove("");
#			if len(b) == 4:
#				if b[3] == "True":
#					b[3] = True;
#				else:
#					b[3] = False;
#				network.sendPacket.Packet0x04(float(b[0]), float(b[1]), float(b[2]), b[3]);
#			else:
#				print("usage: move <x> <y> <z> <onGround>");
#		elif a == "":
#			pass;
#		elif a[:4] == "help":
#			print """stop/quit/exit - halt the program
#getData - Get object data
#move - Move to to a location
#help - guess"""
#		else:
#			print("Invalid command");
#	elif connected == True:
#		print("Connection Terminated");
#		exit();
#	else:
#		print(network.dispatch.bot.loggedIn);
#		time.sleep(1)
