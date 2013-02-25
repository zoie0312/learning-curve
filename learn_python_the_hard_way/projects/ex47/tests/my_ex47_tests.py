from nose.tools import *
from my_ex47 import game

def test_room():
	gold = game.Room("GoldRoom",
				"""This room has gold in it you can grab. There's a door to the
				north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = game.Room("Center", "Test room in the center.")
	north = game.Room("North", "Test room in the north.")
	south = game.Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
	
def test_map():
	start = game.Room("Start", "You can go west and down a hole.")
	west = game.Room("Trees", "There are trees here, you can go east.")
	down = game.Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
	

#def setup():
#	print "SETUP!"
	
#def teardown():
#	print "TEAR DOWN!"
	
#def test_basic():
#	print "I RAN!"