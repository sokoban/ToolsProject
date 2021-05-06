# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from netaddr import *
from socket import *

def portscan(targetip, targetport):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex( ( targetip , int(targetport) ) )

    if result == 0:
        print ('[+] {} , {}/tcp open' .format(targetip,str(targetport) ))
    #else:
        #print ('[+] %s/tcp close' % targetip )
    sock.close()

def All_ipv4_address(subnet):
    ipaddr = IPNetwork(subnet)
    return ipaddr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ip = All_ipv4_address('221.143.42.85/32')
    for i in ip:
        target = str(i)
        print(target)
        portscan(target, 13309)