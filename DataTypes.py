import struct
import Misc
import zlib
compress = False
class Buffer():
    string = ""
    
    def read(self, count):
        if count > len(self.string):
            raise Exception("Reading " + str(count) + ", buffer contains " + str(len(self.string)))
        string = self.string[:count]
        self.string = self.string[count:]
        return string
    
    def readBuffer(self, count):
        buffer = Buffer()
        buffer.addRaw(self.read(count))
        return buffer
    
    def addRaw(self, string):
        self.string += string
    
    def getRaw(self):
        return self.string
    
    def getNextPacket(self):
        if self.string == "": return None
        tmp = self.string
        length = self.readVarInt()
        if length <= len(self.string):
            if compress:
                buff = self.readBuffer(length)
                buff.readVarInt()
                buff.string = zlib.decompress(buff.string, zlib.MAXWBITS)
                return buff
            else:
                return self.readBuffer(length)
        else:
            self.string = tmp
            return None
    
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
        nbtSize = self.readShort()
        if nbtSize == -1: return slot
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
    
    def readVarInt(self):
        number = 0
        reference = 0
        byte = self.readUnsignedByte()
        number += byte & 0x7f
        while(byte >> 7 == 1):
            reference += 1
            byte = self.readUnsignedByte()
            number += (byte & 0x7f) << (7 * reference)
        return number
    
    def readPosition(self):
        val = self.readLong()
        x = val >> 38
        y = val << 26 >> 52
        z = val << 38 >> 38
        return x, y, z

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
    
    def readUnsignedByte(self):
        return struct.unpack("!B", self.read(1))[0]
    


def writeSlot(slot):
    print "data value", slot.dataValue
    if slot == None:
        return writeShort(-1)
    string = writeShort(slot.dataValue)
    string += writeByte(slot.count)
    string += writeShort(slot.damage)
    print "slot", string.encode("hex")
    if slot.nbt == "":
        string += writeShort(-1)
        return string
    string += writeShort(len(slot.nbt))
    string += slot.nbt
    return string

def writeDouble(number):
    return struct.pack("!d", number)

def writeBool(number):
    return struct.pack("!?", number)

def writeFloat(number):
    return struct.pack("!f", number)

def writeVarInt(number):
    string = ""
    char = number & 0x7f
    number = number >> 7
    while(number != 0):
        char = char | 0x80
        string += chr(char)
        char = number & 0x7f
        number = number >> 7
    string += chr(char)
    return string

def writeInt(number):
    return struct.pack("!i", number)

def writeString(string):
    string1 = writeVarInt(len(string))
    string1 += struct.pack("!" + str(len(string)) + "s", string)
    return string1

def writeByte(number):
    return chr(number)

def writeUnsignedByte(number):
    return struct.pack("!B", number)

def writeShort(number):
    return struct.pack("!h", number)

def writeUnsignedShort(number):
    return struct.pack("!H", number)
    
def writeLength(data):
	return writeVarInt(len(data)) + data
