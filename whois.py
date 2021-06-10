# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import whois
from ipwhois import IPWhois

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("TEST")

    obj = IPWhois('74.125.225.229')
    results = obj.lookup_rdap(depth=1)
    print(results)
    #print(obj)

#    domain = "www.naver.com"
#    ret = whois.whois(domain)
 #   print(ret)




