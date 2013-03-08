"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from gothonweb.map import *
#from django.contrib.sessions.backends.db import SessionStore
#from django.conf import settings
#from django.utils.importlib import import_module
from django.test.client import Client
from django.contrib.auth.models import User


#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)


class GothonwebMapTests(TestCase):
    def test_room(self):
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a door to the
				north.""")
	self.assertEqual(gold.name, "GoldRoom")
	self.assertEqual(gold.paths, {})
	
    def test_room_paths(self):
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	self.assertEqual(center.go('north'), north)
	self.assertEqual(center.go('south'), south)
	
    def test_map(self):
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	self.assertEqual(start.go('west'), west)
	self.assertEqual(start.go('west').go('east'), start)
	self.assertEqual(start.go('down').go('up'), start)
	
    def test_gothon_game_map(self):
	self.assertEqual(START.go('shoot'), generic_death)
	self.assertEqual(START.go('dodge'), generic_death)
	
	room = START.go('tell a joke')
	self.assertEqual(room, laser_weapon_armory)
	


class GothonwebViewTests(TestCase):
    def test_root_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_hello_get_view(self):
        response = self.client.get(reverse('gothonweb:hello'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fill Out This Form")

    def test_hello_post_noarg_view(self):
        response = self.client.post(reverse('gothonweb:hello'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "world")

    def test_hello_post_view(self):
        response = self.client.post(reverse('gothonweb:hello'),
                                    {'sname': 'John',
                                     'mygreet': 'Hi'}
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hi, John")
        

class SessionTestCase(TestCase):
    def setUp(self):
        # http://code.djangoproject.com/ticket/10899
        #settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        #engine = import_module(settings.SESSION_ENGINE)
        #store = engine.SessionStore()
        #store.save()
        #self.session = store
        #self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
        self.client = Client()
        User.objects.create_user('john', 'john@gmail.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

class GothonwebGameTests(SessionTestCase):
    def test_game_wo_session_view(self):
        response = self.client.get(reverse('gothonweb:gameengine'))
        #self.assertEqual(response.status_code, 302)
        #self.assertContains(response, "Fill Out This Form")
        self.assertRedirects(response, '/gothonweb/hello/',
                             status_code=302, target_status_code=200, msg_prefix='')        

    def test_game_w_session_view(self):
        session = self.client.session
        session['room'] = START
        session.save()
        #self.client.session = session
        #self.client.session.save()
        response = self.client.get(reverse('gothonweb:gameengine'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Corridor")
        
