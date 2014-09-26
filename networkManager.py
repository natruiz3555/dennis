import socket
import zlib
import DataTypes
import time
import packetDispatch


buff = DataTypes.Buffer()

HOST = 'localhost'
PORT = 25565

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(0)

def writeLength(data):
    return DataTypes.writeVarInt(len(data)) + data

def login():
    global sendData
    packet = "\x00"
    packet += DataTypes.writeVarInt(47)
    packet += DataTypes.writeString(HOST)
    packet += DataTypes.writeUnsignedShort(PORT)
    packet += DataTypes.writeVarInt(2)
    packet = writeLength(packet)
    sendData += packet
    #Next Packet
    packet = '\x00'
    packet += DataTypes.writeString("jem50")
    packet = writeLength(packet)
    sendData += packet


login()
t=0
while True:
    try:
        buff.addRaw(s.recv(16))
    except socket.error, v:
        pass
    if sendData:
        s.send(sendData)
        sendData = ""
    packet = buff.getNextPacket()
    if packet:
        a = hex(packet.readVarInt())
        while len(a) < 4:
            a = "0x0" + a[2:]
        a = a.replace("f", "F")
        print("+" + a)
        pDispatch[a](packet)



