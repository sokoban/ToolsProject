'''
# install :
# usage :
# author : sokoban
'''
from netaddr import *
from socket import *
import requests

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

    f = open("./web_list.txt", "r")

    lines = f.readlines()

    for line in lines:

        url = "https://dodo-prod.s3.us-west-1.amazonaws.com/" + line
        print(url)
        response = requests.get(url)
        #print(response.status_code)
        #print(response.text)
        if response.status_code != 403:
            print(response.text)
        else:
            print("NO")


    f.close()