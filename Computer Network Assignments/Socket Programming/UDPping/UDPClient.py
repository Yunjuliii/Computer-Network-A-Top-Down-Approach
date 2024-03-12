# UDPPingerClient.py 
import datetime
from socket import * 
# Create a UDP socket  
ClientSocket = socket(AF_INET, SOCK_DGRAM) 
ClientSocket.settimeout(5)
#Information of Server
ServerName = '10.218.162.131'
ServerPort = 12000
for num in range(1,11):
    time_send = datetime.datetime.now()
    message = "number is : "+str(num) + " time is a: "+str(datetime.datetime.now())
    ClientSocket.sendto(message.encode(),(ServerName,ServerPort))
    try:
        Backmessage, serveraddress = ClientSocket.recvfrom(2048)
        time_recv = datetime.datetime.now()
        print(Backmessage.decode(),"RTT = %s"%str((time_recv-time_send).total_seconds()))
    except timeout:
        print("request time out")
ClientSocket.close()
              



