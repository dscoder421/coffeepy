from socket import *
import os
from colorama import Fore

def scan():
    target = input("Enter URL: ")
    t_ip = gethostbyname(target)
    os.system("cls")
    print(Fore.CYAN, """
IP for url {} is {}. Do you want to continue(y/n)
    """.format(target, t_ip))
        

# from socket import *
# import time
# startTime = time.time()

# if __name__ == '__main__':
#    target = input('Enter the host to be scanned: ')
#    t_IP = gethostbyname(target)
#    print ('Starting scan on host: ', t_IP)
   
#    for i in range(50, 500):
#       s = socket(AF_INET, SOCK_STREAM)
      
#       conn = s.connect_ex((t_IP, i))
#       if(conn == 0) :
#          print ('Port %d: OPEN' % (i,))
#       s.close()
# print('Time taken:', time.time() - startTime)