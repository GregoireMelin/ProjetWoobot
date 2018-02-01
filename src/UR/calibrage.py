#Role de ce fichier:
#Obtenir les donnees du port serie

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    nb=int(raw_input('Force pour calibrage: '))
    print nb
except ValueError:
    print "Not a number"

#a revoir cf serial csv write
try:
    while(1):
        trame = ser.readline().rstrip()
        print trame
except KeyboardInterrupt:
    raise
