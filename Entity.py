from Location import Location

class Entity():
	
	def __init__(self, ID=None):
		if ID != None:
			self.ID = ID;
	# Location object
	location = Location();
	
	# Location object (velocity of x, y, and z)
	velocity = Location();
	
	# ID of the entity
	ID = None;
	
	# If player is on the ground
	onGround = None;
	
	# Rotation of the player in location object (z-axis ignored)
	rotation = Location();
	
	# status of entity
	#
	# 0	 Something related to living entities?
	# 1	 Something related to the player entity?
	# 2	 Living Entity hurt
	# 3	 Living Entity dead
	# 4	 Iron Golem throwing up arms
	# 6	 Wolf/Ocelot/Horse taming - Spawn "heart" particles
	# 7	 Wolf/Ocelot/Horse tamed - Spawn "smoke" particles
	# 8	 Wolf shaking water - Trigger the shaking animation
	# 9	 (of self) Eating accepted by server
	# 10	 Sheep eating grass
	# 11	 Iron Golem handing over a rose
	# 12	 Villager mating - Spawn "heart" particles
	# 13	 Spawn particles indicating that a villager is angry and seeking revenge
	# 14	 Spawn happy particles near a villager
	# 15	 Witch animation - Spawn "magic" particles
	# 16	 Zombie converting into a villager by shaking violently
	# 17	 Firework exploding
	# 18	 Animal in love (ready to mate) - Spawn "heart" particles 
	entity = None;
	
	# metadata the of entity
	metadata = None;
	
	# array of effect objects that are applied to an entity
	effect = None;
	
	# Properties of an entity in a dictionary
	properties = None;
	
	# If player is in bed
	inBed = None;
	
	#  Block location of the head part of the bed
	bedLocation = Location();
	
	# Animation
	#
	# 0	Swing arm
	# 1	Damage animation
	# 2	Leave bed
	# 3	Eat food
	# 4	Critical effect
	# 5	Magic critical effect
	# 102  (unknown)
	# 104  Crouch
	# 105  Uncrouch 
	animation = None;
	
	# Player user ID
	UUID = None;
	
	#  The item the player is currently holding.
	# Note that this should be 0 for "no item", unlike
	# -1 used in other packets. A negative value crashes clients. 
	currentItem = None;
	
	# ID	 Object   x,z	 y
	#
	# 1	  Boat	 1.5	 0.6
	# 2	  Item Stack (Slot)	 0.25	 0.25
	# 10	 Minecart	 0.98	 0.7
	# 11	 (unused since 1.6.x)	 Minecart (storage)	 0.98	 0.7
	# 12	 (unused since 1.6.x)	 Minecart (powered)	 0.98	 0.7
	# 50	 Activated TNT	 0.98	 0.98
	# 51	 EnderCrystal	 2.0	 2.0
	# 60	 Arrow (projectile)	 0.5	 0.5
	# 61	 Snowball (projectile)	 0.25	 0.25
	# 62	 Egg (projectile)	 0.25	 0.25
	# 63	 FireBall (ghast projectile)	 1.0	 1.0
	# 64	 FireCharge (blaze projectile)	 0.3125	 0.3125
	# 65	 Thrown Enderpearl	 0.25	 0.25
	# 66	 Wither Skull (projectile)	 0.3125	 0.3125
	# 70	 Falling Objects	 0.98	 0.98
	# 71	 Item frames	 varies	 varies
	# 72	 Eye of Ender	 0.25	 0.25
	# 73	 Thrown Potion	 0.25	 0.25
	# 74	 Falling Dragon Egg	 0.98	 0.98
	# 75	 Thrown Exp Bottle	 0.25	 0.25
	# 76	 Firework Rocket	 0.25	 0.25
	# 77	 Leash Knot	 0.5	 0.5
	# 90	 Fishing Float	 0.25	 0.25 
	type = None;

class NonLiving(Entity):
	def __init__(self, ID=None):
		if ID != None:
			Entity.__init__(self, ID);
	title = None;
	direction

class Living(Entity):
	def __init__(self, ID=None):
		if ID != None:
			Entity.__init__(self, ID);

class Player(Living):
	def __init__(self, ID=None):
		if ID != None:
			Entity.__init__(self, ID);
	UUID = "";
	Username = "";
	stats = [];
	location = Location();
	health = None;
	food = None;
	foodSaturation = None;
	# 0: survival, 1: creative, 2: adventure. The hardcore flag is not included 
	gamemode = None;
	slot = None;
	rotation = Location();