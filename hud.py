import sys
import socket
import pygame
import time

speed = 0
rpm = 0
rpm_percentage = 0
gear = 'N'
breaking_lvl = 0
fuel = 0
fuel_percentage = 0
current_time = 0

pygame.init()
win = pygame.display.set_mode((320, 240))
pygame.display.set_caption('Simple HUD')
win.fill((35,35,35))

fg = pygame.font.Font('btf.ttf', 100)
fs = pygame.font.Font('btf.ttf', 60)
fm = pygame.font.Font('btf.ttf', 15)
fb = pygame.font.Font('btf.ttf', 25)

crashed = False
pygame.display.update()
clock = pygame.time.Clock()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.2'
port = 9000
s.connect((host, port))

def hud():
	speed_lbl = fs.render(str(speed), True, (240,240,240))
	speed_lbl_x = (320 - speed_lbl.get_width()) / 2
	win.blit(speed_lbl, (speed_lbl_x, 155))

	mph_lbl = fm.render('MPH', True, (240,240,240))
	mph_lbl_x = (320 - mph_lbl.get_width()) / 2
	win.blit(mph_lbl, (mph_lbl_x, 215))

	rpm_bg = pygame.draw.rect(win, (240,240,240), (0,0,320,55))
	rpm_used = rpm_percentage/100*320
	if rpm_percentage >= 95:
		rpm_bar = pygame.draw.rect(win, (158,0,0,), (0,0,rpm_used,50))
	elif rpm_percentage >= 85:
		rpm_bar = pygame.draw.rect(win, (246,220,46), (0,0,rpm_used,50))
	else:
		rpm_bar = pygame.draw.rect(win, (35,35,35), (0,0,rpm_used,50))

	gear_lbl = fg.render(gear, True, (240,240,240))
	gear_lbl_x = (320 - gear_lbl.get_width()) / 2
	win.blit(gear_lbl, (gear_lbl_x, 55))

	fuel_bg = pygame.draw.rect(win, (240,240,240), (20,60,35,145))
	fuel_used = 141 - (fuel_percentage/100*141)
	if fuel_percentage == 0:
		fuel_bar = pygame.draw.rect(win, (240,240,240), (22,62,31,141))
	elif fuel_percentage <= 5:
		fuel_bar = pygame.draw.rect(win, (158,0,0), (22,62,31,141))
		fuel_bar = pygame.draw.rect(win, (240,240,240), (22,62,31,fuel_used))
	else:
		fuel_bar = pygame.draw.rect(win, (35,35,35), (22,62,31,141))
		fuel_bar = pygame.draw.rect(win, (240,240,240), (22,62,31,fuel_used))
	fuel_lbl = fb.render(str(fuel) + 'L', True, (240,240,240))
	win.blit(fuel_lbl, (22, 205))

	break_bg = pygame.draw.rect(win, (240,240,240), (265,60,35,145))
	break_per = 141 - (breaking_lvl/100*141)
	fuel_bar = pygame.draw.rect(win, (158,0,0), (267,62,31,141))
	fuel_bar = pygame.draw.rect(win, (240,240,240), (267,62,31,break_per))
	fuel_lbl = fb.render('B', True, (240,240,240))
	win.blit(fuel_lbl, (275, 205))


	pygame.display.update()

def getStats():
	global speed, rpm, rpm_percentage, gear, breaking_lvl, fuel, fuel_percentage
	data = s.recv(1024).decode().replace(' ', '')
	data = data.replace(',', '').split(';')
	speed = data[0].replace("'", '')
	rpm = data[1].replace("'", '')
	rpm_percentage = int(data[2].replace("'", ''))
	gear = str(data[3].replace("'", ''))
	breaking_lvl = data[4]
	fuel = data[5]
	fuel_percentage = data[6]

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
            s.close()
			print(event)

	win.fill((32,32,32))
	getStats()
	hud()
	pygame.display.update()
	clock.tick(120)

s.close()