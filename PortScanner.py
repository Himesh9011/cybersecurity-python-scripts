import socket

# AF.INET for IPv4 , SOCK_STREAM for TCP (SYN/ACK logic), 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# timeout so the script doesn't hang on 'Filtered' ports
s.settimeout(2) 

ip = input("Enter the IP : ")
port = int(input("Enter the PORT : "))

# connect_ex returns 0 if the connection is successful (OPEN)
result = s.connect_ex((ip, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    # This could be CLOSED or FILTERED
    print(f"Port {port} is CLOSED or FILTERED")

s.close()

"""In this code we are verifing Open/Closed Port on the basis of code the programm is returnning rather than sending/analyzing the flags like(SYN/ACK/RST)"""
