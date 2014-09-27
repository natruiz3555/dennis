import os
from World import World
from Entity import Player

class Bot(Player):
	def __init__(self):
		Player.__init__(self);
	loggedIn = False;
	joined = False;
	enc = False;
	secret = os.urandom(16);
	world = World();
