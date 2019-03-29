import time
import smbus
import RPi.GPIO as GPIO
import ctypes
import sys

tempuser=sys.argv
tempser=85 #température de service de la bouilloire
exec(open("Allumer17.py").read()) #on allume la bouilloire
while temp<tempser:
        temp=exec(open("./i2carduirasp.py").read()) #on récupère la température de la bouilloire via la carte arduino
exec(open("./Eteindre17.py").read())

exec(open("./Allumer27.py").read()) #on allume la pompe qui transporte l'eau chaude dans la tasse
time.sleep(20) #dans l'idéal on aurait un capteur pour savoir la quantité d'eau versé et pour savoir quand arrêter la pompe
exec(open("./Eteindre27.py").read())

exec(open("./Allumer22.py").read()) #on allume la plaque chauffante sur lequel est posée la tasse
while(tempuser>temp) #Pour la présentation nous n'avions qu'une seule sonde donc on devait déplacer la sonde manuellement entre les deux étapes nous aurions évidemment deux sonde pour le produit fini
        temp=exec(open("./i2carduirasp.py").read())
exec(open("./Allumer24.py").read()) #allume un buzzer pour prévenir que c'est prêt dans l'idéal envoie une notification sur téléphone
while(true) #on considère que l'utilisateur éteins ou redémarre le système quand il prend sa tasse
        if(temp>tempuser): #on cherche à rester dans le domaine d'hysteresis de la temperature utilisateur en alternant
                exec(open("./Eteindre22.py").read())
        else
                exec(open("./Allumer22.py").read())