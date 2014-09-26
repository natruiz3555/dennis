import os
from World import World

class Bot():
    UUID = "";
    loggedIn = False;
    joined = False;
    Username = "";
    enc = False;
    secret = os.urandom(16);
    stats = [];
    world = World();
    location = Location();
    health = None;
    food = None;
    foodSaturation = None;
    # 0: survival, 1: creative, 2: adventure. The hardcore flag is not included 
    gamemode = None;

    
