
import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 


if int(hora) >= 21:
	print ("Es momento de hiser a casa") 
else:
	print ("Te faltan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))