#
#  Copyright 2014 Nathan Ruiz <natruiz3553@gmail.com>
# 
# Dennis is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

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
	def disconnect(self):
		self.network.s.close();
		exit();
