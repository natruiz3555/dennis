import DataTypes
from Bot import Bot
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
bot = Bot()

def Packet0x00(buff):
    KeepAliveID = buff.readVarInt()

def Packet0x02(buff):
    if bot.loggedIn == False:
        bot.UUID = buff.readString()
        bot.Username = buff.readString()
        print("UUID:" + bot.UUID)
        bot.loggedIn = True
    else:
        JSONData = buff.readString()
        Position = buff.readByte()
        print("Chat:" + JSONData)

def Packet0x03(buff):
    Ageoftheworld = buff.readBool()
    Timeofday = buff.readBool()

def Packet0x04(buff):
    EntityID = buff.readVarInt()
    Slot = buff.readShort()
    Item = buff.readBool()

def Packet0x05(buff):
    Location = buff.readPosition()

def Packet0x06(buff):
    Health = buff.readBool()
    Food = buff.readVarInt()
    FoodSaturation = buff.readBool()

def Packet0x07(buff):
    Dimension = buff.readInt()
    Difficulty = buff.readUnsignedByte()
    Gamemode = buff.readUnsignedByte()
    LevelType = buff.readString()

def Packet0x08(buff):
    X = buff.readBool()
    Y = buff.readBool()
    Z = buff.readBool()
    Yaw = buff.readBool()
    Pitch = buff.readBool()
    Flags = buff.readByte()
    X = buff.readBool()
    Y = buff.readBool()
    Z = buff.readBool()
    Y_ROT = buff.readBool()
    X_ROT = buff.readBool()

def Packet0x09(buff):
    Slot = buff.readByte()

def Packet0x0A(buff):
    EntityID = buff.readVarInt()
    Location = buff.readPosition()

def Packet0x0B(buff):
    EntityID = buff.readVarInt()
    Animation = buff.readUnsignedByte()

def Packet0x0C(buff):
    EntityID = buff.readVarInt()
    PlayerUUID = buff.readBool()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()
    Yaw = buff.readByte()
    Pitch = buff.readByte()
    CurrentItem = buff.readShort()
    Metadata = buff.readMetadata()

def Packet0x0D(buff):
    CollectedEntityID = buff.readVarInt()
    CollectorEntityID = buff.readVarInt()

def Packet0x0E(buff):
    EntityID = buff.readVarInt()
    Type = buff.readByte()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()
    Pitch = buff.readByte()
    Yaw = buff.readByte()
    Data = buff.readObjectData()

def Packet0x0F(buff):
    EntityID = buff.readVarInt()
    Type = buff.readUnsignedByte()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()
    Yaw = buff.readByte()
    Pitch = buff.readByte()
    HeadPitch = buff.readByte()
    VelocityX = buff.readShort()
    VelocityY = buff.readShort()
    VelocityZ = buff.readShort()
    Metadata = buff.readMetadata()

def Packet0x10(buff):
    EntityID = buff.readVarInt()
    Title = buff.readString()
    Location = buff.readPosition()
    Direction = buff.readUnsignedByte()

def Packet0x11(buff):
    EntityID = buff.readVarInt()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()
    Count = buff.readShort()

def Packet0x12(buff):
    EntityID = buff.readVarInt()
    VelocityX = buff.readShort()
    VelocityY = buff.readShort()
    VelocityZ = buff.readShort()

def Packet0x13(buff):
    Count = buff.readVarInt()
    EntityIDs = buff.readArrayOfVarInt()

def Packet0x14(buff):
    EntityID = buff.readVarInt()

def Packet0x15(buff):
    EntityID = buff.readVarInt()
    DX = buff.readByte()
    DY = buff.readByte()
    DZ = buff.readByte()
    OnGround = buff.readBool()

def Packet0x16(buff):
    EntityID = buff.readVarInt()
    Yaw = buff.readByte()
    Pitch = buff.readByte()
    OnGround = buff.readBool()

def Packet0x17(buff):
    EntityID = buff.readVarInt()
    DX = buff.readByte()
    DY = buff.readByte()
    DZ = buff.readByte()
    Yaw = buff.readByte()
    Pitch = buff.readByte()
    OnGround = buff.readBool()

def Packet0x18(buff):
    EntityID = buff.readVarInt()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()
    Yaw = buff.readByte()
    Pitch = buff.readByte()
    OnGround = buff.readBool()

def Packet0x19(buff):
    EntityID = buff.readVarInt()
    HeadYaw = buff.readByte()

def Packet0x1A(buff):
    EntityID = buff.readInt()
    EntityStatus = buff.readByte()

def Packet0x1B(buff):
    EntityID = buff.readInt()
    VehicleID = buff.readInt()
    Leash = buff.readBool()

def Packet0x1C(buff):
    EntityID = buff.readVarInt()
    Metadata = buff.readMetadata()

def Packet0x1D(buff):
    EntityID = buff.readVarInt()
    EffectID = buff.readByte()
    Amplifier = buff.readByte()
    Duration = buff.readVarInt()
    HideParticles = buff.readBool()

def Packet0x1E(buff):
    EntityID = buff.readVarInt()
    EffectID = buff.readByte()

def Packet0x1F(buff):
    Experiencebar = buff.readBool()
    Level = buff.readVarInt()
    TotalExperience = buff.readVarInt()

def Packet0x20(buff):
    EntityID = buff.readVarInt()
    Count = buff.readInt()
    Properties = buff.readBool()

def Packet0x21(buff):
    ChunkX = buff.readInt()
    ChunkZ = buff.readInt()
    GroundUpcontinuous = buff.readBool()
    Primarybitmap = buff.readBool()
    Size = buff.readVarInt()
    Data = buff.readBool()

def Packet0x22(buff):
    ChunkX = buff.readInt()
    ChunkZ = buff.readInt()
    Recordcount = buff.readVarInt()
    Records = buff.readBool()

def Packet0x23(buff):
    Location = buff.readPosition()
    BlockID = buff.readVarInt()

def Packet0x24(buff):
    Location = buff.readPosition()
    Byte1 = buff.readUnsignedByte()
    Byte2 = buff.readUnsignedByte()
    BlockType = buff.readVarInt()

def Packet0x25(buff):
    EntityID = buff.readVarInt()
    Location = buff.readPosition()
    DestroyStage = buff.readByte()

def Packet0x26(buff):
    Skylightsent = buff.readBool()
    Chunkcolumncount = buff.readVarInt()
    Metainformation = buff.readBool()
    Data = buff.readBool()

def Packet0x27(buff):
    X = buff.readBool()
    Y = buff.readBool()
    Z = buff.readBool()
    Radius = buff.readBool()
    Recordcount = buff.readInt()
    Records = buff.readBool()
    PlayerMotionX = buff.readBool()
    PlayerMotionY = buff.readBool()
    PlayerMotionZ = buff.readBool()

def Packet0x28(buff):
    EffectID = buff.readInt()
    Location = buff.readPosition()
    Data = buff.readInt()
    Disablerelativevolume = buff.readBool()

def Packet0x29(buff):
    Soundname = buff.readString()
    EffectpositionX = buff.readInt()
    EffectpositionY = buff.readInt()
    EffectpositionZ = buff.readInt()
    Volume = buff.readBool()
    Pitch = buff.readUnsignedByte()

def Packet0x2A(buff):
    ParticleId = buff.readInt()
    LongDistance = buff.readBool()
    X = buff.readBool()
    Y = buff.readBool()
    Z = buff.readBool()
    OffsetX = buff.readBool()
    OffsetY = buff.readBool()
    OffsetZ = buff.readBool()
    Particledata = buff.readBool()
    Numberofparticles = buff.readInt()
    Data = buff.readArrayOfVarInt()

def Packet0x2B(buff):
    Reason = buff.readUnsignedByte()
    Value = buff.readBool()

def Packet0x2C(buff):
    EntityID = buff.readVarInt()
    Type = buff.readByte()
    X = buff.readInt()
    Y = buff.readInt()
    Z = buff.readInt()

def Packet0x2D(buff):
    Windowid = buff.readUnsignedByte()
    InventoryType = buff.readString()
    Windowtitle = buff.readBool()
    NumberofSlots = buff.readUnsignedByte()
    EntityID = buff.readInt()

def Packet0x2E(buff):
    WindowID = buff.readUnsignedByte()

def Packet0x2F(buff):
    WindowID = buff.readByte()
    Slot = buff.readShort()
    Slotdata = buff.readBool()

def Packet0x30(buff):
    slots = []
    WindowID = buff.readUnsignedByte()
    Count = buff.readShort()
    while Count > 0:
        slots.append(buff.readSlot())

def Packet0x31(buff):
    WindowID = buff.readUnsignedByte()
    Property = buff.readShort()
    Value = buff.readShort()

def Packet0x32(buff):
    WindowID = buff.readUnsignedByte()
    Actionnumber = buff.readShort()
    Accepted = buff.readBool()

def Packet0x33(buff):
    Location = buff.readPosition()
    Line1 = buff.readBool()
    Line2 = buff.readBool()
    Line3 = buff.readBool()
    Line4 = buff.readBool()

def Packet0x34(buff):
    ItemDamage = buff.readVarInt()
    Scale = buff.readByte()
    Length = buff.readVarInt()
    Icons = buff.readBool()
    Columns = buff.readByte()
    Rows = buff.readByte()
    X = buff.readByte()
    Y = buff.readByte()
    Length = buff.readVarInt()
    Data = buff.readBool()

def Packet0x35(buff):
    Location = buff.readPosition()
    Action = buff.readUnsignedByte()
    NBTData = buff.readBool()

def Packet0x36(buff):
    Location = buff.readPosition()

def Packet0x37(buff):
    Count = buff.readVarInt()
    while Count > 0:
		Entry = buff.readString()
		Value = buff.readVarInt()
		bot.stats.append({"Entry":Entry, "Value":Value})
		Count -= 1

def Packet0x38(buff):
    Action = buff.readVarInt()
    Length = buff.readVarInt()
    UUID = buff.readBool()
def Packet0x39(buff):
    Flags = buff.readByte()
    Flyingspeed = buff.readBool()
    Walkingspeed = buff.readBool()

def Packet0x3A(buff):
    Count = buff.readVarInt()
    Match = buff.readString()

def Packet0x3B(buff):
    Objectivename = buff.readString()
    Mode = buff.readByte()
    Objectivevalue = buff.readString()
    Type = buff.readString()

def Packet0x3C(buff):
    Scorename = buff.readString()
    UpdateRemove = buff.readByte()
    ObjectiveName = buff.readString()
    Value = buff.readVarInt()

def Packet0x3D(buff):
    Position = buff.readByte()
    ScoreName = buff.readString()

def Packet0x3E(buff):
    TeamName = buff.readString()
    Mode = buff.readByte()
    TeamDisplayName = buff.readString()
    TeamPrefix = buff.readString()
    TeamSuffix = buff.readString()
    Friendlyfire = buff.readByte()
    NameTagVisibility = buff.readString()
    Color = buff.readByte()
    Playercount = buff.readVarInt()
    Players = buff.readBool()

def Packet0x3F(buff):
    Channel = buff.readString()
    Data = buff.readBool()

def Packet0x40(buff):
    Reason = buff.readString()

def Packet0x41(buff):
    Difficulty = buff.readUnsignedByte()

def Packet0x42(buff):
    Event = buff.readVarInt()
    Duration = buff.readVarInt()
    EntityID = buff.readInt()
    PlayerID = buff.readVarInt()
    EntityID = buff.readInt()
    Message = buff.readString()

def Packet0x43(buff):
    CameraID = buff.readVarInt()

def Packet0x44(buff):
    Action = buff.readVarInt()
def Packet0x45(buff):
    Action = buff.readVarInt()
def Packet0x46(buff):
    Threshold = buff.readVarInt()
    print("Got compression")

def Packet0x47(buff):
    Header = buff.readBool()
    Footer = buff.readBool()

def Packet0x48(buff):
    URL = buff.readString()
    Hash = buff.readString()

def Packet0x49(buff):
    EntityID = buff.readVarInt()
    Tag = buff.readBool()

def Packet0x00(buff):
    JSONResponse = buff.readString()

def Packet0x00(buff):
    JSONData = buff.readString()

def Packet0x01(buff):
	if bot.joined:
		if bot.enc:
			Time = buff.readBool()
		else:
			print(buff.string.encode("hex"))
			ServerID = buff.readString()
			PublicKey = buff.readString()
			VerifyToken = buff.readString()
			bot.encryption = True
			bot.cipher = AES.new(bot.secret, AES.MODE_CFB, bot.secret)
			bot.decipher = AES.new(bot.secret, AES.MODE_CFB, bot.secret)
			print(VerifyToken)
			key2 = RSA.importKey(PublicKey)
			key = PKCS1_v1_5.new(key2)
	else:
		EntityID = buff.readInt()
		Gamemode = buff.readUnsignedByte()
		Dimension = buff.readByte()
		Difficulty = buff.readUnsignedByte()
		MaxPlayers = buff.readUnsignedByte()
		LevelType = buff.readString()
		ReducedDebugInfo = buff.readBool()
		bot.joined = True

#def Packet0x03(buff):
#    Threshold = buff.readVarInt()
#    print("Enabling Compression.")
#    DataTypes.compress = True



pDispatch = {
    '0x00':Packet0x00,
    '0x01':Packet0x01,
    '0x02':Packet0x02,
    '0x03':Packet0x03,
    '0x04':Packet0x04,
    '0x05':Packet0x05,
    '0x06':Packet0x06,
    '0x07':Packet0x07,
    '0x08':Packet0x08,
    '0x09':Packet0x09,
    '0x0A':Packet0x0A,
    '0x0B':Packet0x0B,
    '0x0C':Packet0x0C,
    '0x0D':Packet0x0D,
    '0x0E':Packet0x0E,
    '0x0F':Packet0x0F,
    '0x10':Packet0x10,
    '0x11':Packet0x11,
    '0x12':Packet0x12,
    '0x13':Packet0x13,
    '0x14':Packet0x14,
    '0x15':Packet0x15,
    '0x16':Packet0x16,
    '0x17':Packet0x17,
    '0x18':Packet0x18,
    '0x19':Packet0x19,
    '0x1A':Packet0x1A,
    '0x1B':Packet0x1B,
    '0x1C':Packet0x1C,
    '0x1D':Packet0x1D,
    '0x1E':Packet0x1E,
    '0x1F':Packet0x1F,
    '0x20':Packet0x20,
    '0x21':Packet0x21,
    '0x22':Packet0x22,
    '0x23':Packet0x23,
    '0x24':Packet0x24,
    '0x25':Packet0x25,
    '0x26':Packet0x26,
    '0x27':Packet0x27,
    '0x28':Packet0x28,
    '0x29':Packet0x29,
    '0x2A':Packet0x2A,
    '0x2B':Packet0x2B,
    '0x2C':Packet0x2C,
    '0x2D':Packet0x2D,
    '0x2E':Packet0x2E,
    '0x2F':Packet0x2F,
    '0x30':Packet0x30,
    '0x31':Packet0x31,
    '0x32':Packet0x32,
    '0x33':Packet0x33,
    '0x34':Packet0x34,
    '0x35':Packet0x35,
    '0x36':Packet0x36,
    '0x37':Packet0x37,
    '0x38':Packet0x38,
    '0x39':Packet0x39,
    '0x3A':Packet0x3A,
    '0x3B':Packet0x3B,
    '0x3C':Packet0x3C,
    '0x3D':Packet0x3D,
    '0x3E':Packet0x3E,
    '0x3F':Packet0x3F,
    '0x40':Packet0x40,
    '0x41':Packet0x41,
    '0x42':Packet0x42,
    '0x43':Packet0x43,
    '0x44':Packet0x44,
    '0x45':Packet0x45,
    '0x46':Packet0x46,
    '0x47':Packet0x47,
    '0x48':Packet0x48,
    '0x49':Packet0x49,
    '0x00':Packet0x00,
    '0x01':Packet0x01,
    '0x00':Packet0x00,
    '0x01':Packet0x01,
    '0x03':Packet0x03,
}
