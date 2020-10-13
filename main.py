from klawx3.arduino import Arduino


def arduino_listener(data): # callback de arduino
    print("Dato de arduino:", data)

if __name__ == "__main__": # función principal
    puerto = "COM3"
    ard = Arduino(puerto) # parametros de conexión
    ard.add_listener(arduino_listener) # agrega la funcion listener para escuchar datos de arduino
    connected = ard.connect() # inicia la conexión y el thread (modo daemon) interno
    if connected:
        ard.send_data('hola') # envia un 'hola' a arduino
    else:
        print("Sin conexión a arduino")
    
    ard.keep_alive() # mantiene el hilo principal vivo (solo para casos tener listeners) -> CTL+C para terminar





