import rpi_data_acquisition
import time
import socket

UDP_IP = "192.168.3.1"
UDP_PORT = 5005

print("Creating rpi_data_acquisition class...")
tb=rpi_data_acquisition.rpi_data_acquisition()

print("Starting rpi_data_acquisition...")
tb.start()
print("Started...")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print("int(data)=%d" % int(data))
    
    if int(data)==1:
        #time.sleep(0.2)
        tb.set_trigger(1)
        print("started")
#        time.sleep(0.025)
#        tb.set_trigger(-1)
    else:
        tb.set_trigger(-1)       
        print("stopped")
        
    print("")

        
