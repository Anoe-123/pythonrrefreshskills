import time
def change_light(light):
   return light + 1
light = 0
if light == 0:
   print("RED")
   time.sleep(3)
   light = change_light(light)
if light == 1:
   print("RED + AMBER")
   time.sleep(3)
   light = change_light(light)
if light == 2:
   print("GREEN")
   time.sleep(3)
   light = change_light(light)
if light == 3:
   print("AMBER")
   time.sleep(3)