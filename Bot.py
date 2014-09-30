#
#  Copyright 2014 natruiz3553 <natruiz3553@gmail.com>
# 
# McBot is free software: you can redistribute it and/or modify
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

import os
from World import World
from Entity import Player

class Bot(Player):
	def __init__(self):
		Player.__init__(self);
	printable = True;
	loggedIn = False;
	joined = False;
	enc = False;
	comp = False
	compThreshold = 0
	secret = os.urandom(16);
	world = World();
	XP = None;
	level = None;
