import socket
import serial
ser = serial.Serial ("/dev/ttyAMA0")  
ser.baudrate = 9600    

def TCPRPIServer(q):
	RPIHOST, RPIPORT: "lmao idk", 80

	while True:
		RPI2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		RPI2.bind((RPIHOST, RPIPORT))
		RPI2.listen(1)
		conn, addr = RPI2.accept()
		sendata = q.get()
		data = conn.send(sendata)
		RPI2.close()

def PISerial(q):
    
    while True:
        q.put(ser.readline())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target = PISerial, args = (q))
    p2 = Process(target = TCPRPIServer, args = (q))
    p1.start()
    p2.start()
