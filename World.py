class World():
    entities = [];
    blocks = [];
    worldAge = None;
    timeOfDay = None;
    #  0 thru 3 for Peaceful, Easy, Normal, Hard. 
    difficulty = None;
    # default, flat, largeBiomes, amplified, default_1_1
    levelType = None;
    # -1: The Nether, 0: The Overworld, 1: The End 
    dimension = None;