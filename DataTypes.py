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

import struct
import Misc
import zlib
import math
import traceback;
from Location import Location

compress = False
class Buffer():
	
	def __init__(self):
		self.string = ""

	def read(self, count):
		if count > len(self.string):
			raise Exception("Reading " + str(count) + ", buffer contains " + str(len(self.string)))
		string = self.string[:count]
		self.string = self.string[count:]
		return string
	
	def readBuffer(self, count, source=None):
		buffer = Buffer()
		if source == None:
			buffer.addRaw(self.read(count))
		else:
			buffer.addRaw(source.recv(count));
		return buffer
	
	def addRaw(self, string):
		if string != None:
			self.string += string
	
	def getRaw(self):
		return self.string
	
	def getNextPacket(self, compression=-1, source=None):
		if self.string == "" and source == None:
			return None;
		tmp = self.string;
		length = self.readVarInt(source);
		if source != None or length > 0:
			packet = self.readBuffer(length, source);
			if compression == -1:
				return packet;
			uncompressedSize = packet.readVarInt();
			if uncompressedSize >= compression:
				packet.string = zlib.decompress(packet.string);
			return packet;
		else:
			self.string = tmp
			#print("no source");
			return None;
	
	def readObjectData(self):
		objectData = {}
		objectData["id"] = self.readInt()
		if objectData["id"] == 0: return None
		objectData["speedX"] = self.readShort()
		objectData["speedY"] = self.readShort()
		objectData["speedZ"] = self.readShort()
		return objectData
	
	def readSlot(self):
		slot = Misc.Slot()
		slot.dataValue = self.readShort()
		if slot.dataValue == -1: return None
		slot.count = self.readByte()
		slot.damage = self.readShort()
		nbtSize = self.readByte()
		if nbtSize == 0: return slot
		slot.nbt = self.read(nbtSize)
		return slot
	
	def readMetadata(self):
		metadata = {}
		key = self.readUnsignedByte()
		while key != 0x7f:
			index = key & 0x1f
			dataType = key >> 5
			if (dataType == 0): metadata[index]= self.readByte()
			elif (dataType == 1): metadata[index] = self.readShort()
			elif (dataType == 2): metadata[index] = self.readInt()
			elif (dataType == 3): metadata[index] = self.readFloat()
			elif (dataType == 4): metadata[index] = self.readString()
			elif (dataType == 5): metadata[index] = self.readSlot()
			elif (dataType == 6): metadata[index] = (self.readInt(), self.readInt(), self.readInt())
			elif (dataType == 7): metadata[index] = (self.readFloat(), self.readFloat(), self.readFloat())
			else: raise Exception("Unknown enitiy metadata type.")
			key = self.readUnsignedByte()
		return metadata
	
	def readVarInt(self, source=None):
		tmp = self.string
		#try:
		number = 0
		reference = 0
		byte = self.readUnsignedByte(source)
		number += byte & 0x7f
		while byte >> 7 == 1 and reference < 4:
			reference += 1
			byte = self.readUnsignedByte(source)
			number += (byte & 0x7f) << (7 * reference)
		return number
		#except TypeError:
		#	self.string = tmp
		#	return None
		
	def readVarIntandSize(self):
		number = 0
		reference = 0
		byte = self.readUnsignedByte()
		number += byte & 0x7f
		while(byte >> 7 == 1):
			reference += 1
			byte = self.readUnsignedByte()
			number += (byte & 0x7f) << (7 * reference)
		return number, reference + 1
	
	def readPosition(self):
		val = self.readLong()
		x = val >> 38
		y = val << 26 >> 52
		z = val << 38 >> 38
		location = Location();
		location.set(x, y, z);
		return location;

	def readString(self):
		length = self.readVarInt()
		return self.read(length)
	
	def readShort(self):
		return struct.unpack("!h", self.read(2))[0]
	
	def readInt(self):
		return struct.unpack("!i", self.read(4))[0]
	
	def readLong(self):
		return struct.unpack("!q", self.read(8))[0]
	
	def readBool(self):
		return struct.unpack("!?", self.read(1))[0]
	
	def readFloat(self):
		return struct.unpack("!f", self.read(4))[0]
	
	def readDouble(self):
		return struct.unpack("!d", self.read(8))[0]

	def readByte(self):
		return struct.unpack("!b", self.read(1))[0]
	
	def readUnsignedByte(self, source=None):
		if source == None:
			return struct.unpack("!B", self.read(1))[0];
		else:
			data = source.recv(1);	
			return struct.unpack("!B", data)[0];


	def writeSlot(self, slot):
		print "data value", slot.dataValue
		if slot == None:
			self.writeShort(-1);
			return;
		self.writeShort(slot.dataValue);
		self.writeByte(slot.count);
		self.writeShort(slot.damage);
		if slot.nbt == "":
			self.writeShort(-1);
			return;
		self.writeShort(len(slot.nbt))
		self.writeInt(slot.nbt);
	
	def writeDouble(self, number):
		self.string += struct.pack("!d", number);
	
	def writeBool(self, number):
		self.string += struct.pack("!?", number)
	
	def writeFloat(self, number):
		self.string += struct.pack("!f", number)
	
	def writeVarInt(self, number):
		string = ""
		char = number & 0x7f
		number = number >> 7
		while(number != 0):
			char = char | 0x80
			string += chr(char)
			char = number & 0x7f
			number = number >> 7
		string += chr(char)
		self.string += string
	
	def writeInt(self, number):
		self.string += struct.pack("!i", number)
	
	def writeString(self, string):
		self.writeVarInt(len(string));
		self.string += struct.pack("!" + str(len(string)) + "s", string);
	
	def writeByte(self, number):
		self.string += chr(number)
	
	def writeUnsignedByte(self, number):
		self.string += struct.pack("!B", number)
	
	def writeShort(self, number):
		self.string += struct.pack("!h", number)
	
	def writeUnsignedShort(self, number):
		self.string += struct.pack("!H", number)
		
	def networkFormat(self, compressionThreshold=-1):
		string = self.string;
		self.string = "";
		if compressionThreshold != -1:
			if len(string) >= compressionThreshold:
				afterSize = len(string)
				string = zlib.compress(string)
				beforeSize = len(string) + math.floor(math.log(afterSize, 128)) + 1
			else:
				afterSize = 0
				beforeSize = len(string) + 1
			self.writeVarInt(beforeSize)
			self.writeVarInt(afterSize)
			self.addRaw(string)
		else:
			self.writeVarInt(len(string));
			self.addRaw(string);
