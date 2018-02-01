#Role de ce fichier:
#Lire un fichier csv et afficher les donnees sous forme de courbe

import serial
import csv
import time

ser = serial.Serial('/dev/ttyACM1', 9600)

nb_calib_data = 10000
calib_data = nb_calib_data
zero = 0

with open('force_data.csv','wb') as csvfile_to_write:
	writer = csv.writer(csvfile_to_write)
	header = True
	Not_complete_line = False
	start_t = time.time()
	try:
		while(1):
	 		#Removing of the header
			if header:
				header = False
			else:
				print "Calibration", 1/nb_calib_data * 100, "%"
				trame = ser.readline().rstrip()
				data = [float(val) for val in trame.split()]
				print data
				if calib_data > 0:
					zero = zero + (1./nb_calib_data)*data[-1]
					calib_data -= 1
					#print zero
				else:
					print "temps: ",format(time.time()-start_t,'.2f'),"valeurs:", trame
					print data[-1]-zero
					writer.writerow([time.time()-start_t,data[0]])
	except KeyboardInterrupt:
		csvfile_to_write.close()
csvfile_to_write.close()
