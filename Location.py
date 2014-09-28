class Location():
	x = None;
	y = None;
	z = None;
	printable = True;
	def set(self, x, y, z):
		self.x = x;
		self.y = y;
		self.z = z;
	def add(self, x, y, z):
		self.x += x;
		self.y += y;
		self.z += z;