class Entity():
    # Location object
    location = None;
    
    # Location object (velocity of x, y, and z)
    velocity = None;
    
    # ID of the entity
    ID = None;
    
    # If player is on the ground
    onGround = None;
    
    # Rotation of the player in location object (z-axis ignored)
    rotation = None;
    
    # status of entity
    entity = None;
    # 0 	Something related to living entities?
    # 1 	Something related to the player entity?
    # 2 	Living Entity hurt
    # 3 	Living Entity dead
    # 4 	Iron Golem throwing up arms
    # 6 	Wolf/Ocelot/Horse taming - Spawn "heart" particles
    # 7 	Wolf/Ocelot/Horse tamed - Spawn "smoke" particles
    # 8 	Wolf shaking water - Trigger the shaking animation
    # 9 	(of self) Eating accepted by server
    # 10 	Sheep eating grass
    # 11 	Iron Golem handing over a rose
    # 12 	Villager mating - Spawn "heart" particles
    # 13 	Spawn particles indicating that a villager is angry and seeking revenge
    # 14 	Spawn happy particles near a villager
    # 15 	Witch animation - Spawn "magic" particles
    # 16 	Zombie converting into a villager by shaking violently
    # 17 	Firework exploding
    # 18 	Animal in love (ready to mate) - Spawn "heart" particles 
    
    # metadata the of entity
    metadata = None;
    
    # array of effect objects that are applied to an entity
    effect = None;
    
    # Properties of an entity in a dictionary
    properties = None;