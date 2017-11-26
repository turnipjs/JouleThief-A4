import game
import entities
import pygame
import json
import levels

class LevelExample(levels.Level):
	def on_setup(self):
		# self.add_entity(entities.ParralaxScroller(path="asset/sky.png", factor=0.1, x=174, y=357, obey_gravity=False, is_solid=False, can_collide=False))
		self.add_entity(entities.ParralaxScroller(image=pygame.image.load("asset/something.gif"), factor=0, x=174, y=357, obey_gravity=False, is_solid=False, can_collide=False))
		self.add_entity(entities.ParralaxScroller(path="asset/stars.png", factor=0.05, x=174, y=357, obey_gravity=False, is_solid=False, can_collide=False))

		self.add_entity(entities.ParralaxScroller(path="asset/buildings1.png", factor=0.1, x=174, y=550, obey_gravity=False, is_solid=False, can_collide=False))
		self.add_entity(entities.ParralaxScroller(path="asset/buildings2.png", factor=0.4, x=174, y=550, obey_gravity=False, is_solid=False, can_collide=False))
		self.add_entity(entities.ParralaxScroller(path="asset/buildings3.png", factor=0.8, x=174, y=550, obey_gravity=False, is_solid=False, can_collide=False))
		self.load_level("asset/parallax_room.png")
		self.create_player((300,300))
		self.add_entity(entities.SimpleImageEntity(path="asset/redsquare.png", x=200, y=740)).on_collided_with=lambda o:self.game.set_state(LevelExample2())
		self.enable_scrolling()

class LevelExample2(levels.Level):
	def on_setup(self):
		self.load_level("asset/sample-level.png")
		self.create_player((200,200))
		self.add_entity(entities.SimpleImageEntity(path="asset/redsquare.png", x=400, y=400)).on_collided_with=lambda o:self.game.set_state(LevelExample())