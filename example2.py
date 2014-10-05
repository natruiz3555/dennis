#!/usr/bin/python2
#
#  Copyright 2014 Darcy Ryan <darcy150@gmail.com>
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

from networkManager import NetworkManager
import socket;
import thread;
import types;
import zlib;
import DataTypes;
from pprint import pprint

network = NetworkManager('localhost', 25565, 'Thebot', 'password')
network.login()

while True:
	network.handleNewPackets(network);
	network.sendWaitingPackets();
