import smbus
import time


       ## Import GPIO library
def call_i2c_arduino(address, nbBytes):
        print "Demande Arduino ",address
        bus.write_byte(address, nbBytes)
        # Pause de 1 seconde pour laisser le temps au traitement de se faire
        time.sleep(1)

        print "La reponse de l'arduino : "
        reponse = bus.read_i2c_block_data(address, 0, nbBytes)
        reponsestr = []
        for i in range(len(reponse)):
                reponsestr.append(str(reponse[i]))
        mystr = ''.join(reponsestr)
        #fichier=open("/var/www/html/data.txt","w")
        fichier=open("data.txt", 'w')
        fichier.write(mystr)
        fichier.close()
        return mystr


# Remplacer 0 par 1 si nouveau Raspberry
bus = smbus.SMBus(1)
address1 = 0x01
address2 = 0x02
nbBytes = 1

call_i2c_arduino(address1,nbBytes)