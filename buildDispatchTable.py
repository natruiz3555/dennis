import requests
from BeautifulSoup import BeautifulSoup

print("[+]Downloading Protocol from Wiki...")
soup = BeautifulSoup(requests.get("http://wiki.vg/Protocol").text)
f = open("./packetDispatch.py", "w")
tables = soup.findAll("table", { "class" : "wikitable" })
wfile = ""
x=0
tab = "	"
disp = "pDispatch = {\n"
def getDataType(dt):
	if dt == "VarInt":
		return "buff.readVarInt()"
	elif dt == "Byte":
		return "buff.readByte()"
	elif dt == "Int":
		return "buff.readInt()"
	elif dt == "Object Data":
		return "buff.readObjectData()"
	elif dt == "Unsigned Byte":
		return "buff.readUnsignedByte()"
	elif dt == "Short":
		return "buff.readShort()"
	elif dt == "Metadata":
		return "buff.readMetadata()"
	elif dt == "String":
		return "buff.readString()"
	elif dt == "Position":
		return "buff.readPosition()"
	elif dt == "Unsigned Byte":
		return "buff.readUnsignedByte()"
	elif dt == "Array of VarInt":
		return "buff.readArrayOfVarInt()"
	elif dt == "Boolean" or "Bool":
		return "buff.readBoolean()"
	elif dt == "Float":
		return "buff.readFloat()"
	elif dt == "Array of Property Data":
		return "buff.readArrayOfPropertyData()"
	elif dt == "Byte Array":
		return "buff.readByteArray()"
	elif dt == "Slot":
		return "buff.readSlot()"
	else:
		return "buff.error() #Unknown Data Type!"
print("[+]Building...")
for table in tables:
	try:
		cells = []
		for row in table.findAll("tr"):
			cells.append(row.findAll("td"))
		if cells[1][2].text != "Client":
			continue
		defstm = "def Packet" + cells[1][0].text + "(buff):\n"
		disp += tab + "'" + cells[1][0].text + "':" + "Packet" + cells[1][0].text + ",\n"
		wfile += defstm
		line = tab + cells[1][3].text.replace(" ", "").replace("-", "").replace("/", "") + " = " + getDataType(cells[1][4].text) + "\n"
		wfile += line
		for field in cells[2:]:
			line = tab + field[0].text.replace(" ", "").replace("-", "").replace("/", "") + " = " + getDataType(field[1].text) + "\n"
			wfile += line
		wfile += "\n"
	except IndexError:
		pass
wfile += "\n\n" + disp + "}"
f.write(wfile)
f.close
print("[+]Done!")
