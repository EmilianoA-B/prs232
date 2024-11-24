import serial 
from datetime import date
try:
    portA = serial.Serial('Puerto')
    fecha = date.today()
    fecha = "Fecha de transmision: " + fecha.strftime("%d/%m/%Y")
    archivo = open("LogP3-escrito.txt","a")
    archivo.write(fecha+"\n")
    print("Inicio de transmisión, para salir escriba .exit")
    message = ""

    while message != ".exit":
        message = str(input("$ "))+"\n"
        portA.write((message+"\n").encode())
        archivo.write("Sent: " + message)
    archivo.write("Comuncación finalizada")
    
except:
    print("Configuracion erronea de puerto, intenta otra vez")



    



    

    
