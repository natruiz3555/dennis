from networkManager import NetworkManager;
from Location import Location;
from time import sleep;
import math;
class Dennis():
        def __init__(self, host, port, username, password):
		self.host = host;
		self.port = port;
		self.username = username;
		self.password = password;
		self.network = NetworkManager(host, port, username, password);
	def login(self):
		self.network.login();
	def goTo(self, x, y, z):
		old = self.network.dispatch.bot.location;
		distance = Location();
		distance.x = x-old.x;
		distance.z = z-old.z;
		speed = 3/20;
		vx = speed * math.sin(math.tanh(distance.z/distance.x));
		vz = speed * math.cos(math.tanh(distance.z/distance.x));
		self.network.X = vx;
		self.network.Z = vz;
		if x > old.x:
			while self.network.dispatch.bot.location.x < x:
				sleep(0.05);
		elif x < old.x:
			while self.network.dispatch.bot.location.x > x:
				sleep(0.05);
		self.network.X = 0;
		self.network.Z = 0;
