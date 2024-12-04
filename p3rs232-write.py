import serial 
from datetime import datetime 
try:
    portA = serial.Serial(
        port='COM10',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        rtscts=True              
                          )
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
        portA.reset_input_buffer()
        portA.reset_output_buffer()
    archivo.write("\n---------Comuncacion finalizada---------\n")
    
except Exception:
    print("Configuracion erronea de puerto, intenta otra vez")