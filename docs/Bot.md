Methods
=======

Connection
----------
* login(server, port, username, password)
 * Manages connections to the server
 * @param string server
   * IP of the server to connect to
 * @param int port
   * Port of the minecraft server
 * @param string username
   * Username to use
 * @param string password
   * Password for the bot to use
 * @param boolean offline
   * True if running in offline mode
 * @return True if successful
* disconnect()

Blocks, mining, building
------------------------
* walkTo(location)
* sendChat(message)
 * @param string message
   * Message to send to the server console
* breakBlock(location) - breaks block with currently held item
* findBlock(blockID)
 * @param int blockID
   * the kind of block to find
 * @return the location of the block int a location object if found, false if else
* placeBlock(location) - Places the currently held block at a location
 * @return false if object is not placable. 
* attack(entity)
* jump()
* setSneak(isSneaking)
* eat()
* useItem()
* switchItem()
* chooseItemSlot(slotId)
* craftItem(itemId) 
* toContainer(inventorySlot, containerSlot, container) - Move item from bots inventory into a container.
* fromContainer(inventorySlot, containerSlot, container) - Move item from container into bots inventory
* placeSign(text, location, axis)
* findNearest()
* findPlayer(playerName)
 * @return A players x y z in location object
* findNearestEntity() - gets an entity object for the closest entity from the bot

Properties
----------
* players = []
* entities = [array of entityclassess]
* world = World() #world class

