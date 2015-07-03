# import sys
# import time
# import socket

# sys.path.insert(len(sys.path), 'apps/python/SimpleHUD/SimpleHUD')
# from sim_info import info


# #--- SERVER --
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = '192.168.0.2'
# port = 9000

# s.connect((host, port))
# while True:

# #--- RPM --
# 	rpm = info.physics.rpms
# 	max_rpm = info.static.maxRpm
# 	if rpm != 0:
# 		rpm_percent = int(rpm/max_rpm*100)
# 	else:
# 		rpm_percent = 0

# #--- SPEED ---
# 	speed = int(info.physics.speedKmh/1.609344)

# #--- GEAR ---
# 	gear = info.physics.gear - 1
# 	if gear == 0:
# 		gear = str("N")
# 	elif gear < 0:
# 		gear = str("R")

# #--- FUEL ---
# 	fuel = info.physics.fuel
# 	max_fuel = info.static.maxFuel
# 	if fuel != 0:
# 		fuel_percent = int(fuel/max_fuel*100)
# 	else:
# 		fuel_percent = 0

# #--- BRAKING ---
# 	brake = info.physics.brake
# 	braking_lvl = int(brake/100*10000)

# #--- LAP ---
# 	current_time = info.graphics.currentTime

# #--- SEND DATA ---
# 	time.sleep(.1)
# 	#print_data = 'Speed: ', speed, 'RPM: ', rpm_percent, 'Gear: ', gear, 'Braking: ', braking_lvl, 'Fuel: ', fuel, fuel_percent,'Lap Time: ', current_time
# 	send_data = (speed, ';', rpm, ';', rpm_percent, ';', gear, ';', braking_lvl, ';', fuel, ';', fuel_percent, ';', current_time)
# 	s.send(str(send_data).encode())
# 	print(send_data)
# s.close()

import sys
import time
import socket

sys.path.insert(len(sys.path), 'apps/python/SimpleHUD/SimpleHUD')
from sim_info import info


#--- SERVER --
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.2'
port = 9000
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()
print ('Got connection from', addr)
while True:

#--- RPM --
	rpm = info.physics.rpms
	max_rpm = info.static.maxRpm
	if rpm != 0:
		rpm_percent = int(rpm/max_rpm*100)
	else:
		rpm_percent = 0

#--- SPEED ---
	speed = int(info.physics.speedKmh/1.609344)

#--- GEAR ---
	gear = info.physics.gear - 1
	if gear == 0:
		gear = str("N")
	elif gear < 0:
		gear = str("R")

#--- FUEL ---
	fuel = info.physics.fuel
	max_fuel = info.static.maxFuel
	if fuel != 0:
		fuel_percent = int(fuel/max_fuel*100)
	else:
		fuel_percent = 0

#--- BRAKING ---
	brake = info.physics.brake
	braking_lvl = int(brake/100*10000)

#--- LAP ---
	current_time = info.graphics.currentTime

#--- SEND DATA ---
	time.sleep(.1)
	#print_data = 'Speed: ', speed, 'RPM: ', rpm_percent, 'Gear: ', gear, 'Braking: ', braking_lvl, 'Fuel: ', fuel, fuel_percent,'Lap Time: ', current_time
	send_data = (speed, ';', rpm, ';', rpm_percent, ';', gear, ';', braking_lvl, ';', fuel, ';', fuel_percent)
	conn.send(str(send_data).encode())
	print(send_data)
s.close()