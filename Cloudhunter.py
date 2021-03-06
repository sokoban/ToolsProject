#!/usr/bin/python

import requests, sys, optparse, os

OKBLUE = '\033[94m'
OKRED = '\033[91m'
OKGREEN = '\033[92m'
OKORANGE = '\033[93m'
COLOR1 = '\033[95m'
COLOR2 = '\033[96m'
RESET = '\x1b[0m'


def logo():
    version = "1.0"
    print('')
    print('             _/                            _/  _/                              _/                          ')
    print('    _/_/_/  _/    _/_/    _/    _/    _/_/_/  _/_/_/    _/    _/  _/_/_/    _/_/_/_/    _/_/    _/  _/_/   ')
    print(' _/        _/  _/    _/  _/    _/  _/    _/  _/    _/  _/    _/  _/    _/    _/      _/_/_/_/  _/_/        ')
    print('_/        _/  _/    _/  _/    _/  _/    _/  _/    _/  _/    _/  _/    _/    _/      _/        _/           ')
    print(' _/_/_/  _/    _/_/      _/_/_/    _/_/_/  _/    _/    _/_/_/  _/    _/      _/_/    _/_/_/  _/            ')
    print('')
    print(OKORANGE + " + -- --=[CloudHunter by 1N3 - https://crowdshield.com" + RESET)
    print(RESET)


logo()
if len(sys.argv) < 2:
    print("You need to specify a domain to check. Use --help for all options.")
    quit()
else:
    parser = optparse.OptionParser()
    parser.add_option('-d', '--domain',
                      action="store", dest="domain",
                      help="Domain name to test", default="")

    parser.add_option('-w', '--wordlist',
                      action="store", dest="wordlist",
                      help="Wordlist of domains to test", default="")

    parser.add_option('-v', '--verbose',
                      action="store", dest="verbose",
                      help="Turn on verbose logging", default="")

options, args = parser.parse_args()
target = str(options.domain)
wordlist = str(options.wordlist)
verbose = str(options.verbose)
cloudfronturl = 'http://coach.fitbit.com'

if (len(wordlist) > 4):
    with open(wordlist) as f:
        urls = f.read().splitlines()
        for url in urls:

            if verbose == 'y':
                print(url)

            # LOOKING FOR CNAME S3 BUCKETS ON TARGET URL ###########################################################
            try:
                if verbose == 'y':
                    print("Looking for CloudFront CNAME's pointing to " + url)
                headers = {'Host': '%s' % url}
                params = ''
                r = requests.get(cloudfronturl, params=params, headers=headers)
                resp = r.text

                if "ListBucketResult" in str(resp):
                    print(
                        OKRED + '[+] 1 Host ' + url + ' has a CloudFront CNAME record pointing to a public S3 bucket!' + RESET)
                    if verbose == 'y':
                        print(resp)

            except:
                pass

            # LOOKING FOR TOP LEVEL S3 BUCKETS ON TARGET URL ########################################################
            try:
                if verbose == 'y':
                    print('Checking for public S3 bucket on https://' + url + '.s3.amazonaws.com')
                r2 = requests.get('https://' + url + '.s3.amazonaws.com', timeout=2)
                resp2 = r2.text

                if "ListBucketResult" in str(resp2):
                    print(
                        OKRED + '[+] 2 Host ' + url + ' has a public S3 bucket registered to the url https://' + url + '.s3.amazonaws.com!' + RESET)
                    if verbose == 'y':
                        print(resp2)

            except:
                pass

            # LOOKING FOR TOP LEVEL S3 BUCKETS ON TARGET URL ########################################################
            try:
                keyword = url.split(".")[-2]
                url3 = 'https://' + keyword + '.s3.amazonaws.com'
                if verbose == 'y':
                    print('Checking for public S3 bucket on ' + url3)
                r3 = requests.get('https://' + keyword + '.s3.amazonaws.com', timeout=2)
                resp3 = r3.text

                if "ListBucketResult" in str(resp3):
                    print(
                        OKRED + '[+] 3 Host ' + url + ' has a public S3 bucket registered to the url https://' + keyword + '.s3.amazonaws.com!' + RESET)
                    if verbose == 'y':
                        print(resp3)

            except:
                pass

            # LOOKING FOR DIRECT S3 BUCKETS ON TARGET URL ############################################################
            try:
                r4 = requests.get('https://' + url, timeout=2)
                resp4 = r3.text
                if verbose == 'y':
                    print('Checking for public S3 bucket on https://' + url)

                if "ListBucketResult" in str(resp4):
                    print(
                        OKRED + '[+] 4 Host ' + url + ' has a public S3 bucket registered to the url https://' + url + '.s3.amazonaws.com!' + RESET)
                    if verbose == 'y':
                        print(resp4)

            except Exception as ex:
                pass

else:

    if verbose == 'y':
        print(target)

    # LOOKING FOR CNAME S3 BUCKETS ON TARGET URL ###########################################################
    try:
        if verbose == 'y':
            print("Looking for CloudFront CNAME's on " + target)
        headers = {'Host': '%s' % target}
        params = ''
        r = requests.get(cloudfronturl, params=params, headers=headers)
        resp = r.text

        if "ListBucketResult" in str(resp):
            print(
                OKRED + '[+] Host ' + target + ' has a CloudFront CNAME record pointing to a public S3 bucket!' + RESET)
            if verbose == 'y':
                print(resp)

    except:
        pass

    # LOOKING FOR TOP LEVEL S3 BUCKETS ON TARGET URL ########################################################
    try:
        if verbose == 'y':
            print('Checking for public S3 bucket on https://' + target + '.s3.amazonaws.com')
        r2 = requests.get('https://' + target + '.s3.amazonaws.com', timeout=2)
        resp2 = r2.text

        if "ListBucketResult" in str(resp2):
            print(
                OKRED + '[+] Host ' + target + ' has a public S3 bucket registered to the target https://' + target + '.s3.amazonaws.com!' + RESET)
            if verbose == 'y':
                print(resp2)

    except:
        pass

    # LOOKING FOR TOP LEVEL S3 BUCKETS ON TARGET URL ##########################################################
    try:
        keyword = target.split(".")[-2]
        target3 = 'https://' + keyword + '.s3.amazonaws.com'
        if verbose == 'y':
            print('Checking for public S3 bucket on ' + target3)
        r3 = requests.get('https://' + keyword + '.s3.amazonaws.com', timeout=2)
        resp3 = r3.text

        if "ListBucketResult" in str(resp3):
            print(
                OKRED + '[+] Host ' + target + ' has a public S3 bucket registered to the url https://' + keyword + '.s3.amazonaws.com!' + RESET)
            if verbose == 'y':
                print(resp3)

    except:
        pass

    # LOOKING FOR DIRECT S3 BUCKETS ON TARGET URL ############################################################
    try:
        r4 = requests.get('https://' + target, timeout=2)
        resp4 = r3.text
        if verbose == 'y':
            print('Checking for public S3 bucket on https://' + target)

        if "ListBucketResult" in str(resp4):
            print(
                OKRED + '[+] Host ' + target + ' has a public S3 bucket registered to the url https://' + target + '!' + RESET)
            if verbose == 'y':
                print(resp4)

    except Exception as ex:
        pass