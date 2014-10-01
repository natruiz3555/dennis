import DataTypes
import zlib
import sys

successCount = 0
failureCount = 0
x = None
y = None
z = None
try: mode = sys.argv[1]
except IndexError: mode = "all"

def test(outcome, name):
    global x, y, z, successCount, failureCount
    assert outcome == True or outcome == False
    if outcome:
        successCount += 1
        if(mode != "fail"):
            print "[PASSED] " + name
    else:
        failureCount += 1
        print "[FAILED] " + name
    x, y, z = None, None, None

print "\n"

#get a packet from buffer
x = DataTypes.Buffer()
x.string = "\x0e\x00testPacket!!!"
test(x.getNextPacket().string == "testPacket!!!", "Reading a packet from buffer")


#get a compressed packet
x = DataTypes.Buffer()
x.string = "\x16\x0dx\x9c+I-.\tHL\xceN-QTT\x04\x00#\xc4\x04|"
test(x.getNextPacket().string == "testPacket!!!", "Reading a compressed packet from buffer")


#send uncompressed packet
x = DataTypes.Buffer()
x.string = "testPacket!!!"
x.networkFormat(128)
test(x.string == "\x0e\x00testPacket!!!", "Sending an uncompressed packet")

#send a compressed packet
x = DataTypes.Buffer()
x.string = "testPacket!!!"
x.networkFormat(2)
test(x.string == "\x16\x0dx\x9c+I-.\tHL\xceN-QTT\x04\x00#\xc4\x04|", "Sending a compressed packet")



print "\nTesting complete: " + str(successCount) + " passes, " + str(failureCount) + " fails.\n"