import serial 
from datetime import datetime 
try:
    portA = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        rtscts=True
        )
    fecha = datetime.now()
    fecha = "Fecha de recepcion: " + fecha.strftime("%d/%m/%Y - %H:%M:%S")
    archivo = open("LogP3-remoto.txt","a")
    archivo.write(fecha+"\n\n")
    archivo.write("\n---------Inicio de escucha---------\n")
    print("Inicio de escucha de mensajes")
    message = ""

    while message != ".exit\n":
        message = portA.readline().decode()
        print(">>> " + message, end="")
        archivo.write("\tListened: " + message)
        portA.reset_input_buffer()
        portA.reset_output_buffer()
    archivo.write("\n---------Finalizacion de transimicion---------\n")

except Exception:
    print("Configuracion erronea de puerto, intenta otra vez")