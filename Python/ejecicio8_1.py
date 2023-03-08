f = open ('Archivo1.txt', 'w')
f.write("Hola Mundo mi primer documento\n")
f.close()


f = open ('Archivo1.txt', 'a+')
f.readline()
f.writelines("Hola Mundo mi segundo documento\n")
f.close()
