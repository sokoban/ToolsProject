'''
# ipwhois :
# install : https://ipwhois.readthedocs.io/en/latest/README.html
# usage :
# author : sokoban

asn_registry : apnic
asn : 9318
asn_cidr : 221.140.0.0/14
asn_country_code : KR
asn_date : 2003-05-30
asn_description : SKB-AS SK Broadband Co Ltd, KR
query : 221.143.42.85
'''
import logging
import socket
from ipwhois import IPWhois

LOG_FORMAT = ('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] '
              '[%(funcName)s()] %(message)s')
logging.basicConfig(level=logging.ERROR  , format=LOG_FORMAT)
log = logging.getLogger(__name__)


def validIPAddress(IP):
    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4: return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Other"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    f = open("./iplist.txt", "r")
    lines = f.readlines()

    for line in lines:
        ip = line.rstrip('\n')
        valid = validIPAddress(ip)

        if valid == "Other":

            if ip.find("http://") or ip.find("https://"):
                ip = ip.lstrip("http://")
                ip = ip.lstrip("https://")

            # 175.126.123.247:8000 process
            if ip.find(':'):
                ret = ip.split(sep=':')
                ip = ret[0]
                valid = validIPAddress(ip)

            if valid == "Other":
                if ip.find('/'):
                    ret = ip.split(sep='/')
                    ip = ret[0]

                if ip.find('?'):
                    ip = ip.strip('?')
                ip = ip.strip('"')
                domain = ip

                try:
                    ip = socket.gethostbyname(ip)
                    domain = domain + ":" + ip
                except:
                    print('{0} Domain host resolve Fail'.format(ip))
                    continue

        try:
            log.debug('Basic str test: {0}'.format(ip))
            obj = IPWhois(ip)
            results = obj.lookup_rdap(depth=1)
            if valid == "Other":
                print('{0} : asn_registry : {1}, asn_cidr : {2}, asn_Country : {3}, date : {4}, desc : {5} '
                    .format(domain, results['asn_registry'], results['asn_cidr'], results['asn_country_code'], results['asn_date'], results['asn_description']))
            else:
                print('{0} : asn_registry : {1}, asn_cidr : {2}, asn_Country : {3}, date : {4}, desc : {5} '
                    .format(ip, results['asn_registry'], results['asn_cidr'], results['asn_country_code'], results['asn_date'], results['asn_description']))
        except:
            if valid == "Other":
                print('{0} ip whois Fail'.format(domain))
            else:
                print('{0} ip whois Fail'.format(ip))
            continue