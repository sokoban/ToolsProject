import pandas
import requests
import requests as r
import re
import urllib3
import sys
import os

urllib3.disable_warnings()

path = input("enter filepath: ")

list = []
file1 = open(path, 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character

for line in Lines:
    ip = line.strip()
    try:
        r = requests.get(ip + ".s3.amazonaws.com", allow_redirects=True, verify=False)

        A = "AccessDenied"
        B = "NoSuchKey"
        C = "NoSuchBucket"
        D = "ListBucketResult"
        E = "PermanentRedirect"
        f = open('out.txt', 'a')
        if A in r.text:
            print("Bucket Found: ", ip, ":", A)
            L = ["Bucket Found: ", ip, ":", A, '\n']
            f.writelines(L)
            f.close()

        elif B in r.text:
            print("Bucket does not exist: ", B, ":", ip)
            L = ["Bucket does not exist: ", B, ":", ip, '\n']
            f.writelines(L)
            f.close()

        elif C in r.text:
            print("Bucket does not exist: ", C, ":", ip)
            L = ["Bucket does not exist: ", C, ":", ip, '\n']
            f.writelines(L)
            f.close()
        elif D in r.text:
            print("Bucket Found: ", D, ":", ip)
            L = ["Bucket Found: ", D, ":", ip, '\n']
            f.writelines(L)
            f.close()

        elif E in r.text:
            print("Bucket does not exist: ", ip, ":", F)
            L = ["Bucket does not exist: ", ip, ":", F, '\n']
            f.writelines(L)
            f.close()
        else:
            print("Bucket Not found :", ip)
            L = ["Bucket Not found :", ip, '\n']
            f.writelines(L)
            f.close()

    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        print("Error: {}".format(e))

