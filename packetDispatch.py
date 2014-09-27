from Bot import Bot
from Entity import Entity
from World import World
from Location import Location
from Effect import Effect
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from DataTypes import *
class PacketDispatch():
    sendData = []
    bot = Bot()
    # Keep alive
    def __init__(self):
        pass
    def Packet0x00(self, buff):
        KeepAliveID = buff.readVarInt()
        print("Keep alive")

    # Alive: Chat update
    # Dead: login info
    def Packet0x02(self, buff):
        if bot.loggedIn == False:
            bot.UUID = buff.readString()
            bot.Username = buff.readString()
            print("Logged in with info:")
            print("\tUUID: " + bot.UUID)
            print("\tUsername: " + bot.Username)
            bot.loggedIn = True
            print("Login Successfull")
        else:
            JSONData = buff.readString()
            Position = buff.readByte()
            print("Chat:" + JSONData)

    # Time update/Set compression
    def Packet0x03(self, buff):
        if bot.loggedIn:
            bot.comp = True
            bot.compThreshold = buff.readVarInt()
        bot.world.worldAge = buff.readLong()
        bot.world.timeOfDay = buff.readLong()

    # Entity Equipment
    def Packet0x04(self, buff):
        EntityID = buff.readVarInt()
        Slot = buff.readShort()
        Item = buff.readBool()
        
        entity = bot.world.getEntity(EntityID);
        entity.slot = Slot;
        entity.item = Item;

    # Spawn Position 
    def Packet0x05(self, buff):
        Bot.location = buff.readPosition();

    # Update Health
    def Packet0x06(self, buff):
        bot.health = buff.readBool();
        bot.food = buff.readVarInt();
        bot.foodSaturation = buff.readBool();

    # Respawn
    def Packet0x07(self, buff):
        Bot.world.dimension = buff.readInt()
        bot.world.difficulty = buff.readUnsignedByte()
        bot.gamemode = buff.readUnsignedByte()
        bot.world.levelType = buff.readString()
        
    # Player position and look
    def Packet0x08(self, buff):
        X = buff.readDouble()
        Y = buff.readDouble()
        Z = buff.readDouble()
        Yaw = buff.readFloat()
        Pitch = buff.readFloat()
        Flags = buff.readByte()
        
        if Flags%2 != 0:
            X += bot.location.x;
            Flags -= 1;
        Flags >>= 1;
        if Flags%2 != 0:
            Y += bot.location.y;
            Flags -= 1;
        Flags >>= 1;
        if Flags%2 != 0:
            Z += bot.location.z;
            Flags -= 1;
        Flags >>= 1;
        if Flags%2 != 0:
            Yaw += bot.rotation.x;
            Flags -= 1;
        Flags >>= 1;
        if Flags%2 != 0:
            Pitch += bot.rotation.y;
            Flags -= 1;
            
        bot.rotation.set(Yaw, Pitch, 0);
        bot.location.set(X, Y, Z);
        

    # Held item changed
    def Packet0x09(self, buff):
        bot.slot = buff.readByte()

    # Use bed
    def Packet0x0A(self, buff):
        EntityID = buff.readVarInt();
        Location = buff.readPosition();
        entity = bot.world.getEntity(EntityID);
        entity.bedLocation = Location;

    # Animation
    def Packet0x0B(self, buff):
        EntityID = buff.readVarInt()
        Animation = buff.readUnsignedByte()
        entity = bot.world.getEntity(EntityID);
        entity.animation = Animation;
        
    # Spawn player
    def Packet0x0C(self, buff):
        EntityID = buff.readVarInt()
        PlayerUUID = buff.readBool()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()
        Yaw = buff.readByte()
        Pitch = buff.readByte()
        CurrentItem = buff.readShort()
        Metadata = buff.readMetadata()
        
        entity = bot.world.getEntity(EntityID);
        entity.UUID = PlayerUUID;
        entity.location.set(X, Y, Z);
        entity.rotation.set(Yaw, Pitch, 0);
        entity.currentItem = CurrentItem;
        entity.metadata = Metadata;

    # Collect item
    def Packet0x0D(self, buff):
        CollectedEntityID = buff.readVarInt()
        CollectorEntityID = buff.readVarInt()

    #
    def Packet0x0E(self, buff):
        EntityID = buff.readVarInt()
        Type = buff.readByte()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()
        Pitch = buff.readByte()
        Yaw = buff.readByte()
        Data = buff.readObjectData() # Add this later
        
        entity = bot.world.getEntity(EntityID);
        entity.type = Type;
        entity.location.set(X, Y, Z);
        entity.rotation.set(Yaw, Pitch, 0);
        
    # Spawn mob
    def Packet0x0F(self, buff):
        EntityID = buff.readVarInt()
        Type = buff.readUnsignedByte()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()
        Yaw = buff.readByte()
        Pitch = buff.readByte()
        HeadPitch = buff.readByte() # No idea what this is
        VelocityX = buff.readShort()
        VelocityY = buff.readShort()
        VelocityZ = buff.readShort()
        Metadata = buff.readMetadata()
        
        entity = bot.world.getEntity(EntityID);
        entity.type = Type;
        entity.location.set(X, Y, Z);
        entity.rotation.set(Yaw, Pitch, 0);
        entity.velocity.set(VelocityX, VelocityY, VelocityZ);
        entity.metadata = Metadata;

    def Packet0x10(self, buff):
        EntityID = buff.readVarInt()
        Title = buff.readString()
        Location = buff.readPosition()
        Direction = buff.readUnsignedByte()

    def Packet0x11(self, buff):
        EntityID = buff.readVarInt()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()
        Count = buff.readShort()

    def Packet0x12(self, buff):
        EntityID = buff.readVarInt()
        VelocityX = buff.readShort()
        VelocityY = buff.readShort()
        VelocityZ = buff.readShort()

    def Packet0x13(self, buff):
        Count = buff.readVarInt()
        EntityIDs = []
        while Count > 0:
            EntityIDs.append(self, buff.readVarInt())
            Count -= 1

    def Packet0x14(self, buff):
        EntityID = buff.readVarInt()

    def Packet0x15(self, buff):
        EntityID = buff.readVarInt()
        DX = buff.readByte()
        DY = buff.readByte()
        DZ = buff.readByte()
        OnGround = buff.readBool()

    def Packet0x16(self, buff):
        EntityID = buff.readVarInt()
        Yaw = buff.readByte()
        Pitch = buff.readByte()
        OnGround = buff.readBool()

    def Packet0x17(self, buff):
        EntityID = buff.readVarInt()
        DX = buff.readByte()
        DY = buff.readByte()
        DZ = buff.readByte()
        Yaw = buff.readByte()
        Pitch = buff.readByte()
        OnGround = buff.readBool()

    def Packet0x18(self, buff):
        EntityID = buff.readVarInt()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()
        Yaw = buff.readByte()
        Pitch = buff.readByte()
        OnGround = buff.readBool()

    def Packet0x19(self, buff):
        EntityID = buff.readVarInt()
        HeadYaw = buff.readByte()

    def Packet0x1A(self, buff):
        EntityID = buff.readInt()
        EntityStatus = buff.readByte()

    def Packet0x1B(self, buff):
        EntityID = buff.readInt()
        VehicleID = buff.readInt()
        Leash = buff.readBool()

    def Packet0x1C(self, buff):
        EntityID = buff.readVarInt()
        Metadata = buff.readMetadata()

    def Packet0x1D(self, buff):
        EntityID = buff.readVarInt()
        EffectID = buff.readByte()
        Amplifier = buff.readByte()
        Duration = buff.readVarInt()
        HideParticles = buff.readBool()

    def Packet0x1E(self, buff):
        EntityID = buff.readVarInt()
        EffectID = buff.readByte()

    def Packet0x1F(self, buff):
        Experiencebar = buff.readBool()
        Level = buff.readVarInt()
        TotalExperience = buff.readVarInt()

    def Packet0x20(self, buff):
        EntityID = buff.readVarInt()
        Count = buff.readInt()
        Properties = buff.readBool()

    def Packet0x21(self, buff):
        ChunkX = buff.readInt()
        ChunkZ = buff.readInt()
        GroundUpcontinuous = buff.readBool()
        Primarybitmap = buff.readBool()
        Size = buff.readVarInt()
        Data = buff.readBool()

    def Packet0x22(self, buff):
        ChunkX = buff.readInt()
        ChunkZ = buff.readInt()
        Recordcount = buff.readVarInt()
        Records = buff.readBool()

    def Packet0x23(self, buff):
        Location = buff.readPosition()
        BlockID = buff.readVarInt()

    def Packet0x24(self, buff):
        Location = buff.readPosition()
        Byte1 = buff.readUnsignedByte()
        Byte2 = buff.readUnsignedByte()
        BlockType = buff.readVarInt()

    def Packet0x25(self, buff):
        EntityID = buff.readVarInt()
        Location = buff.readPosition()
        DestroyStage = buff.readByte()

    def Packet0x26(self, buff):
        buff.string = ""
    #    Skylightsent = buff.readBool()
    #    Chunkcolumncount = buff.readVarInt()
    #    while Chunkcolumncount > 0:
    #        CX = buff.readInt()
    #        CZ = buff.readInt()
    #        PBitmap = buff.readShort()
    #        Data = buff.readString()
    #        Chunkcolumncount -= 1

    def Packet0x27(self, buff):
        X = buff.readBool()
        Y = buff.readBool()
        Z = buff.readBool()
        Radius = buff.readBool()
        Recordcount = buff.readInt()
        Records = buff.readBool()
        PlayerMotionX = buff.readBool()
        PlayerMotionY = buff.readBool()
        PlayerMotionZ = buff.readBool()

    def Packet0x28(self, buff):
        EffectID = buff.readInt()
        Location = buff.readPosition()
        Data = buff.readInt()
        Disablerelativevolume = buff.readBool()

    def Packet0x29(self, buff):
        Soundname = buff.readString()
        EffectpositionX = buff.readInt()
        EffectpositionY = buff.readInt()
        EffectpositionZ = buff.readInt()
        Volume = buff.readBool()
        Pitch = buff.readUnsignedByte()

    def Packet0x2A(self, buff):
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

    def Packet0x2B(self, buff):
        Reason = buff.readUnsignedByte()
        Value = buff.readBool()

    def Packet0x2C(self, buff):
        EntityID = buff.readVarInt()
        Type = buff.readByte()
        X = buff.readInt()
        Y = buff.readInt()
        Z = buff.readInt()

    def Packet0x2D(self, buff):
        Windowid = buff.readUnsignedByte()
        InventoryType = buff.readString()
        Windowtitle = buff.readBool()
        NumberofSlots = buff.readUnsignedByte()
        EntityID = buff.readInt()

    def Packet0x2E(self, buff):
        WindowID = buff.readUnsignedByte()

    def Packet0x2F(self, buff):
        WindowID = buff.readByte()
        Slot = buff.readShort()
        Slotdata = buff.readSlot()

    def Packet0x30(self, buff):
        slots = []
        WindowID = buff.readUnsignedByte()
        Count = buff.readShort()
        while Count > 0:
            slots.append(self, buff.readSlot())
            Count -= 1

    def Packet0x31(self, buff):
        WindowID = buff.readUnsignedByte()
        Property = buff.readShort()
        Value = buff.readShort()

    def Packet0x32(self, buff):
        WindowID = buff.readUnsignedByte()
        Actionnumber = buff.readShort()
        Accepted = buff.readBool()

    def Packet0x33(self, buff):
        Location = buff.readPosition()
        Line1 = buff.readBool()
        Line2 = buff.readBool()
        Line3 = buff.readBool()
        Line4 = buff.readBool()

    def Packet0x34(self, buff):
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

    def Packet0x35(self, buff):
        Location = buff.readPosition()
        Action = buff.readUnsignedByte()
        NBTData = buff.readBool()

    def Packet0x36(self, buff):
        Location = buff.readPosition()

    def Packet0x37(self, buff):
        Count = buff.readVarInt()
        while Count > 0:
            Entry = buff.readString()
            Value = buff.readVarInt()
            bot.stats.append({"Entry":Entry, "Value":Value})
            Count -= 1

    def Packet0x38(self, buff):
        '''
        Action = buff.readVarInt()
        if Action == 0:
            length = buff.readVarInt()
            UUID =  buff.readLong() + buff.readLong()
            while length > 0:
                props = []
                name = buff.readString()
                numofPro = buff.readVarInt()
                while numofPro > 0:
                    prop = []
                    pname = buff.readString()
                    prop.append(pname)
                    pvalue = buff.readString()
                    prop.append(pbalue)
                    isSinged = buff.readBool()
                    if isSinged:
                        signic = buff.readString()
                        prop.append(signic)
                    props.append(prop)
                    numofPro -= 1
                length -= 1
                gamemode = buff.readVarInt()
                ping = buff.readVarInt()
                if buff.readBool():
                    displayName = buff.readString()
                    posit = buff.readByte()
        elif Action == 1:
            length = buff.readVarInt()
            UUID =  buff.readLong() + buff.readLong()
            while length > 0:
                gamemode = buff.readVarInt()
                length -= 1
        elif Action == 2:
            length = buff.readVarInt()
            UUID =  buff.readLong() + buff.readLong()
            while length > 0:
                ping = buff.readVarInt()
                length -= 1
        elif Action == 3:
            length = buff.readVarInt()
            UUID =  buff.readLong() + buff.readLong()
            while length > 0:
                hasDisplayName = buff.readBool()
                if hasDisplayName:
                    displayName = buff.readString()
                    posit = buff.readByte()
                length -= 1
        elif Action == 4:
            length = buff.readVarInt()
            UUID =  buff.readLong() + buff.readLong()
            print("EROROROROROR")
        Length = buff.readVarInt()
        UUID = buff.readBool()'''
        pass

    def Packet0x39(self, buff):
        Flags = buff.readByte()
        Flyingspeed = buff.readFloat()
        Walkingspeed = buff.readFloat()

    def Packet0x3A(self, buff):
        Count = buff.readVarInt()
        Match = buff.readString()

    def Packet0x3B(self, buff):
        Objectivename = buff.readString()
        Mode = buff.readByte()
        Objectivevalue = buff.readString()
        Type = buff.readString()

    def Packet0x3C(self, buff):
        Scorename = buff.readString()
        UpdateRemove = buff.readByte()
        ObjectiveName = buff.readString()
        Value = buff.readVarInt()

    def Packet0x3D(self, buff):
        Position = buff.readByte()
        ScoreName = buff.readString()

    def Packet0x3E(self, buff):
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

    def Packet0x3F(self, buff):
        Channel = buff.readString()
        Data = buff.readString()
    def Packet0x40(self, buff):
        Reason = buff.readString()
        print("Kicked from Server:" + Reason)

    def Packet0x41(self, buff):
        Difficulty = buff.readUnsignedByte()

    def Packet0x42(self, buff):
        Event = buff.readVarInt()
        Duration = buff.readVarInt()
        EntityID = buff.readInt()
        PlayerID = buff.readVarInt()
        EntityID = buff.readInt()
        Message = buff.readString()

    def Packet0x43(self, buff):
        CameraID = buff.readVarInt()

    def Packet0x44(self, buff):
        Action = buff.readVarInt()
        if Action == 0:
            Radios = buff.readDouble()
        elif Action == 1:
            OldRadius = buff.readDouble()
            newRadius = buff.readDouble()
            speed = buff.readVarLong()
        elif Action == 2:
            x = buff.readDouble()
            z = buff.readDouble()
        elif Action == 3:
            x = buff.readDouble()
            z = buff.readDouble()
            oldRadius = buff.readDouble()
            newRadius = buff.readDouble()
            portalTeleBound = buff.readVarInt()
            warningTime = buff.readVarInt()
            warningBlocks = buff.readVarInt()
        elif Action == 4:
            warningTime = buff.readVarInt()
        elif Action == 5:
            wanringBlocks = buff.readVarInt()
    def Packet0x45(self, buff):
        Action = buff.readVarInt()
    def Packet0x46(self, buff):
        Threshold = buff.readVarInt()
        print("Got compression")

    def Packet0x47(self, buff):
        Header = buff.readBool()
        Footer = buff.readBool()

    def Packet0x48(self, buff):
        URL = buff.readString()
        Hash = buff.readString()

    def Packet0x49(self, buff):
        EntityID = buff.readVarInt()
        Tag = buff.readBool()

    def Packet0x00(self, buff):
        global sendData
        keepAlive = buff.readVarInt()
        resp = "\x00"
        resp += writeVarInt(keepAlive)
        resp = writeLength(resp)
        sendData.append(resp)

    def Packet0x01(self, buff):
        if bot.joined:
            if bot.enc:
                Time = buff.readBool()
            else:
                print(self, buff.string.encode("hex"))
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

    #def Packet0x03(self, buff):
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
