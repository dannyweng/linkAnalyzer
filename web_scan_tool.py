#! /usr/bin/env python

import urlScan, unShortenLink, virusTotal

user_input = unShortenLink.shortenLink(input("Please provide a link you want analyzed : \n\n"))

# Comment out any of the tools below if you don't want the output from certain tools:

urlScan.urlScanFunc(user_input)    # urlScan.io
virusTotal.vtFunc(user_input)    # VirusTotal

print('The script opened up a few tabs for you to review.\n\
fyi: it takes urlscan about a whole minute to scan the site so wait a minute and refresh page')