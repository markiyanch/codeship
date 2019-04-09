import os

os.system('pip install -r requirements.txt')
#!/usr/bin/env python
kmh = int(raw_input("Enter km/h: "))
mph =  0.6214 * kmh
print "Speed:", kmh, "KM/H = ", mph, "MPH"