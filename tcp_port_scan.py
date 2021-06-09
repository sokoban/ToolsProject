# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from netaddr import *
from socket import *

def portscan(targetip, targetport):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(1)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Port Reuse option
    sock.bind(('0.0.0.0', 53))
    result = sock.connect_ex( ( targetip , targetport ) )

    if result == 0:
        print ('[+] {} , {} tcp open' .format(targetip, targetport ))
    #else:
        #print ('[+] {} , {} tcp close' .format(targetip, targetport ))
    sock.close()

def All_ipv4_address(subnet):
    ipaddr = IPNetwork(subnet)
    return ipaddr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    f = open("./iplist.txt", "r")
    fr = open("./portlist.txt", "r")
    lines = f.readlines()
    ports = fr.readlines()
    for line in lines:
        #print(line)
        ip = All_ipv4_address(line)
        print(ip)
        for i in ip:
            for port in ports:
                target = str(i)
                try:
                    portscan(target, int(port))
                except:
                    print ('[+] {} , {} tcp Scan Fail' .format(target, port ))
    f.close()