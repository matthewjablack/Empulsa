# import numpy
import pygame
from pygame.locals import *
# import random
# import pyganim
from button import Button
# from pet import Pet
 


class Game:
	running = True

	def __init__(self,size):
		pygame.init();
		
		self.screen = pygame.display.set_mode(size)

	def main(self):
		mainClock = pygame.time.Clock()
		self.screen.fill((240,240,240))
		
		# self.screen.blit(pygame.image.load('banana.gif').convert_alpha(), (240,220))



		outdoors = 0

		exp = 20

		trophy_1 = 1
		trophy_2 = 3
		trophy_3 = 9

		showHearts = 0

		petLittle = 1
		petEvolve = 0



		deviceOn = 0
		deviceTurningOn = 0
		deviceTurningOff = 0

		deviceSleep = 0


		petSleeping = 0


		helloMsg = 0
		morningMsg = 0



		selection_list = []
		active_selection = 0


		giveFood = 0

		petJump = 0


		pygame.display.update()


		while self.running:

			self.font = pygame.font.Font("MyriadPro-Bold.ttf",26)

			pygame.display.set_caption('AmiGO')
			bg = pygame.image.load('background_2.png')
			self.screen.blit(bg, (0, 0))


			if petJump == 0:
				if outdoors == 0:
					if petLittle == 0:
						self.screen.blit(pygame.image.load('images/pet_1/tmp-2.gif'), (30, 120))
					else:
						self.screen.blit(pygame.image.load('images/pet_6/tmp-2.gif'), (30, 120))
				else:
					self.screen.blit(pygame.image.load('images/pet_2/tmp-2.gif'), (30, 120))
			else:
				if outdoors == 0:
					if petLittle == 0:
						self.screen.blit(pygame.image.load('images/pet_1/tmp-' + str(petJump) + '.gif'), (30,120))
					else:
						self.screen.blit(pygame.image.load('images/pet_6/tmp-' + str(petJump) + '.gif'), (30,120))
				else:
					self.screen.blit(pygame.image.load('images/pet_2/tmp-' + str(petJump) + '.gif'), (30,120))
				petJump +=1
				if petJump == 39:
					petJump = 0


			if giveFood > 0:
				if outdoors == 0:
					self.screen.blit(pygame.image.load('images/pet_3/tmp-' + str(giveFood) + '.gif'), (30,120))
				else:
					self.screen.blit(pygame.image.load('images/pet_4/tmp-' + str(giveFood) + '.gif'), (30,120))
				giveFood += 1
				if giveFood == 29:
					exp -= 5
					trophy_3 += 1
					if trophy_3 == 10:
						trophy_3 = 0
						trophy_2 += 1
					giveFood = 0


			if petSleeping > 0:
				self.screen.blit(pygame.image.load('images/pet_5/tmp-' + str((petSleeping) / 10) + '.gif'), (30,120))
				petSleeping += 1
				if petSleeping == 30:
					petSleeping = 1

			if petEvolve > 0:
				self.screen.blit(pygame.image.load('images/pet_7/tmp-' + str(petEvolve) + '.gif'), (30,120))
				petEvolve += 1
				if petEvolve == 78:
					petEvolve = 0
					petLittle = 0


			# if evolve > 0:
			# 	self.screen.blit(pygame.image.load('images/pet_6/tmp-' + str(evolve) + '.gif'), (30,120))
			# 	evole += 1






			self.buttons = []

			self.add_button("images/button_0.png", 50, 550)
			self.add_button("images/button_1.png", 160, 550)
			self.add_button("images/button_2.png", 280, 550)
			self.add_button("images/button_3.png", 420, 550)
			self.add_button_small("images/on_off_button.png", 35, 43)

			# self.screen.blit(pygame.image.load('images/pet.png'), (180,240))

			# self.screen.blit(pygame.image.load('images/sun.png'), (31,119))
			# self.screen.blit(pygame.image.load('images/sun_part_1.png'), (112,119))
			# self.screen.blit(pygame.image.load('images/sun_part_2.png'), (103,147))
			# self.screen.blit(pygame.image.load('images/sun_part_3.png'), (87,175))
			# self.screen.blit(pygame.image.load('images/sun_part_4.png'), (60,198))
			# self.screen.blit(pygame.image.load('images/sun_part_5.png'), (32,212))

			self.screen.blit(pygame.image.load('images/battery-icon.png'), (47, 134))

			self.screen.blit(pygame.image.load('images/button_up.png'), (78,300))
			self.screen.blit(pygame.image.load('images/button_down.png'), (78,412))

			self.screen.blit(pygame.image.load('images/trophy_1.png'), (440,240))
			self.screen.blit(pygame.image.load('images/trophy_2.png'), (440,320))
			self.screen.blit(pygame.image.load('images/trophy_3.png'), (440,400))

			self.screen.blit(pygame.image.load('images/name.png'), (190,130))

			self.screen.blit(pygame.image.load('images/exp.png'), (415,130))

			self.screen.blit(self.font.render(str(exp) + ' Exp', True, (255,255,255)), (427, 147))

			self.screen.blit(self.font.render(str(trophy_1), True, (255,255,255)), (471, 255))
			self.screen.blit(self.font.render(str(trophy_2), True, (255,255,255)), (471, 335))
			self.screen.blit(self.font.render(str(trophy_3), True, (255,255,255)), (471, 415))



			if showHearts == 1:
				self.screen.blit(pygame.image.load('images/chat_bubble_1.png'), (190,130))
				self.screen.blit(self.font.render("Thanks for feeding me.", True, (255,255,255)), (223, 140))
				self.screen.blit(self.font.render("I feel great!", True, (255,255,255)), (240, 170))
				self.screen.blit(pygame.image.load('images/heart_small.png'), (385,170))
				self.screen.blit(pygame.image.load('images/heart_small.png'), (415,170))
				self.screen.blit(pygame.image.load('images/heart_small.png'), (445,170))

			if helloMsg == 1:
				self.screen.blit(pygame.image.load('images/chat_bubble_1.png'), (190,130))
				self.screen.blit(self.font.render("Hey Great Job !!!", True, (255,255,255)), (255, 140))
				self.screen.blit(self.font.render("Your earned 5 exp points !", True, (255,255,255)), (205, 170))
			


			for i in range(0,3):
				if i == active_selection:
					self.screen.blit(pygame.image.load('images/selector_'+str(i)+'.png'), (45,340))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.MOUSEBUTTONDOWN:
					for i in range(0,5):
						b = self.buttons[i]
						if b.pressed(event.pos):
							b.action(i)
							print("{0} button pressed!".format(i))
							
							if i == 0:
								if active_selection != 0:
									active_selection -= 1
								else:
									active_selection = 2
							if i == 1:
								if active_selection != 2:
									active_selection += 1
								else:
									active_selection = 0

							if i == 2:
								if active_selection == 0:
									showHearts = 0

							if i == 3:
								if active_selection == 0:
									showHearts = 1
								elif active_selection == 1:
									giveFood = 1
								elif active_selection == 2:
									if petJump == 0:
										petJump = 1

							if i == 4:
								if deviceSleep == 0:
									deviceSleep = 1
								else:
									deviceSleep = 0

				elif event.type == pygame.KEYDOWN:
					if event.key == K_o:
						if deviceOn == 0:
							deviceTurningOn = 255
						if deviceOn == 1:
							deviceTurningOff = 1
					if event.key == K_j:
						if petJump == 0:
							petJump = 1
					if event.key == K_i:
						if outdoors == 0:
							outdoors = 1
						else:
							outdoors = 0
					if event.key == K_s:
						if petSleeping == 0:
							petSleeping = 1
						else:
							petSleeping = 0
					if event.key == K_m:
						if helloMsg == 0:
							helloMsg = 1
						elif helloMsg == 1:
							helloMsg = 0
					if event.key == K_x:
						exp += 5
					# if event.key == K_n:
					# 	if newMsg == 0:
					# 		newMsg = 1
					# 	elif newMsg == 1:
					# 		newMsg = 0
					if event.key == K_e:
						petEvolve = 1




			if deviceOn == 0:
				if deviceTurningOn > 0:
					if deviceTurningOn > 5:
						background = pygame.image.load('images/screen_background.png').convert()
						background.set_alpha(deviceTurningOn)
						self.screen.blit(background, (31,120))
						deviceTurningOn -= 5
					else: 
						deviceTurningOn = 0
						deviceOn = 1
				
				else:
					background = pygame.image.load('images/screen_background.png')
					self.screen.blit(pygame.image.load('images/screen_background.png'), (31,120))
			if deviceOn == 1:
				if deviceTurningOff > 0:
					if deviceTurningOff < 250:
						background = pygame.image.load('images/screen_background.png').convert()
						background.set_alpha(deviceTurningOff)
						self.screen.blit(background, (31,120))
						deviceTurningOff += 5
					else: 
						deviceTurningOff = 0
						deviceOn = 0


			if deviceSleep == 1:
				pygame.time.wait(250)
				self.screen.blit(pygame.image.load('images/screen_background.png'), (31,120))







					
				# self.screen.fill((0,0,0))
			# else:
				

			



							



			mainClock.tick(60)

			pygame.display.update()


	def add_button(self,filename, x,y):
		b = Button(x, y, 76,76 ,filename, self.action)
		b.display(self.screen)
		self.buttons.append(b)

	def add_button_small(self,filename, x,y):
		b = Button(x, y, 50,50 ,filename, self.action)
		b.display(self.screen)
		self.buttons.append(b)

	def action(self, index):
		if index == 0:
			print "test"





if __name__ == '__main__':
	Game((563, 650)).main()
