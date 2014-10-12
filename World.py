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

from Entity import Entity, Living, NonLiving, Player, Orb

class World():
	entities = [];
	blocks = [];
	worldAge = None;
	timeOfDay = None;
	printable = True;
	#  0 thru 3 for Peaceful, Easy, Normal, Hard. 
	difficulty = None;
	# default, flat, largeBiomes, amplified, default_1_1
	levelType = None;
	# -1: The Nether, 0: The Overworld, 1: The End 
	dimension = None;
	
	blocks = {};
	# Gets an entity object with ID. Creates
	# one if no other object matches the ID
	def getEntity(self, ID):
		for entity in self.entities:
			if ID == entity.ID:
				return entity;
		entity = Entity(ID);
		self.entities.append(entity)
		return entity;
	
	def getLiving(self, ID):
		for entity in self.entities:
			if ID == entity.ID and isinstance(entity, Living):
				return entity;
		entity = Living(ID);
		self.entities.append(entity)
		return entity;
	
	def getNonLiving(self, ID):
		for entity in self.entities:
			if ID == entity.ID and isinstance(entity, NonLiving):
				return entity;
		entity = NonLiving(ID);
		self.entities.append(entity)
		return entity;
	
	def getPlayer(self, ID):
		for entity in self.entities:
			if ID == entity.ID and isinstance(entity, Player):
				return entity;
		entity = Player(ID);
		self.entities.append(entity)
		return entity;
	
	def getOrb(self, ID):
		for entity in self.entities:
			if ID == entity.ID and isinstance(entity, Orb):
				return entity;
		entity = Player(ID);
		self.entities.append(entity)
		return entity;
	
	def delEntity(self, entity):
		if isinstance(entity, int):
			entity = self.getEntity(entity);
		self.entities.remove(entity);
