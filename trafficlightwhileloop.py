import time
def change_light(light):
   return light + 1
light = 0
while light < 4:
   if light == 0:
       print("RED")
   elif light == 1:
       print("RED + AMBER")
   elif light == 2:
       print("GREEN")
   else:
       print("AMBER")
   time.sleep(3)
   light = change_light(light)
