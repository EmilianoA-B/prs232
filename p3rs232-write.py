import serial 
from datetime import datetime 
try:
    portA = serial.Serial('COM8')
    fecha = datetime.now()
    fecha = "Fecha de transmision: " + fecha.strftime("%d/%m/%Y - %H:%M:%S")
    archivo = open("LogP3-local.txt","a")
    archivo.write(fecha+"\n\n")
    archivo.write("\n---------Inicio de transmicion---------\n")
    print("Inicio de transmision, para salir escriba .exit")
    message = ""

    while message != ".exit\n":
        message = str(input("$ ")+"\n")
        portA.write((message).encode())
        archivo.write("\tSent: " + message)
    archivo.write("\n---------Comuncacion finalizada---------\n")
    
except Exception:
    print("Configuracion erronea de puerto, intenta otra vez")