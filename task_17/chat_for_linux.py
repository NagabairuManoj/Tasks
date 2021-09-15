import pyfiglet # For showing the letters on command terminal
import threading # For enabling the sending and receiving the messages at the same time
import socket # for sending the messages through the sockets
import os

os.system("clear")

title = pyfiglet.figlet_format("Welcome to Chat Program", font ="digital")
print(title)
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
print()

YourIP = input("Enter your IP :-")
YourPort = int(input("Enter your PortNumber :-"))
FrndIP = input("Enter your Friend IP :-")
FrndPort = int(input("Enter your Friend PortNumber :-"))
# This helps to send the messages to our friend IP

def sender():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        print("You:-",end='')
        x = input().encode()
        s.sendto(x,(FrndIP,FrndPort))
        if x.decode()== "exit" or x.decode() == "bye":
            os._exit(1)

# This helps to receive the messages from our friend


def reciver():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((YourIP,YourPort))
    while True:
        x = s.recvfrom(1024)
        if x[0].decode() == "exit":
            print('\n',end='')
            os._exit(1)
        else:
            print("\n\t\t\tYourfrnd:-"+x[0].decode()+"\nYou:-",end='')

# This is for assigning  two threads for two functions(sender, receiver )
y1 = threading.Thread( target=sender )
y2 = threading.Thread( target=reciver )

# This is for starting the threads

y1.start()
y2.start()
