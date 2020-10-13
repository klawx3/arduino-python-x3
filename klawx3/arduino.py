# libreria requerida
# pip install pyserial
import signal
import sys
import time
import threading
import serial
import types
from serial.serialutil import SerialException

class Arduino:
    CONECTION_WAIT_TIME = 2.5

    def __init__(self,port,bitrate = 9600):
        self.port = port
        self.bitrate = bitrate        
        self.listeners = []
        self.connected = False
        self.serial = None
        self.thread = None
        self.running = False
        signal.signal(signal.SIGINT, self.__signal_handler)

    def connect(self):
        print("Arduino:","Intentando conexión a ->",self.port) # change this to logger
        try:
            if self.serial == None:
                self.serial = serial.Serial(self.port,self.bitrate)
                self.running = True
                self.connected = True
                self.__start_thread()
                time.sleep(self.CONECTION_WAIT_TIME) # wait arduino to connect
                self.is_connected()
                print("Arduino:","Conexion:",self.is_connected()) # change this to logger
                return self.is_connected()
            else:
                return False
        except SerialException as e:
            raise ArduinoException(e)
            
    def disconnect(self):
        if self.serial != None:
            if self.serial.isOpen():                
                self.serial.close() # serial close

        self.running = False # thread stop
        self.connected = False
        #self.serial = None

    def send_data(self,data):
        if self.is_connected():
            mod_data = data.encode('ascii')
            self.serial.write(mod_data)

    def is_connected(self):
        try:
            return self.serial.isOpen()
        except:
            return False

    def add_listener(self,callback):
        if self.__check_if_instance_is_function(callback):
            self.listeners.append(callback)

    def remove_listener(self,callback):
        if self.__check_if_instance_is_function(callback):
            self.listeners.remove(callback)

    def __check_if_instance_is_function(self,callback):
        if isinstance(callback, types.FunctionType):
            return True
        else:
            raise ValueError('listener must be a function with 1 param')

    def keep_alive(self):
        while self.running:
            time.sleep(0.5)
    
    def __start_thread(self):
        if self.thread == None:
            self.thread = threading.Thread(target=self.__main_thread,args=(self.__fire_event,))
            self.thread.daemon = True
            self.thread.start()

    def __fire_event(self,data):
        for listener in self.listeners:
            listener(data) # fire to every listener

    def __signal_handler(self,signal, frame):
        print('CTR + C Detected -> Exiting App...')
        self.disconnect()
        sys.exit(0)

    def __main_thread(self,internal_fire_event):
        print("Arduino:","Iniciando hilo de arduino")
        while self.running:
            try: 
                data = self.serial.readline()
                formated_data = data.decode('ascii').strip() 
                internal_fire_event(formated_data)
            except:
                pass

class ArduinoException(Exception):
    pass