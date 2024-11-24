import serial 
from datetime import date
try:
    portA = serial.Serial('Puerto')
    fecha = date.today()
    fecha = "Fecha de recepción: " + fecha.strftime("%d/%m/%Y")
    archivo = open("LogP3-recibido.txt","a")
    archivo.write(fecha+"\n")
    print("Inicio de escucha de mensajes")
    message = ""

    while message != ".exit":
        message = portA.readline().decode()
        print()
        archivo.write("Listened: " + message)
    archivo.write("Finalización de")

except:
    print("Configuracion erronea de puerto, intenta otra vez")



    



    

    
