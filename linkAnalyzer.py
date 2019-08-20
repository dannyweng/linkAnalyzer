#! /usr/bin/env python

# Link Analyzer Script/Toolkit
# Author: Danny Weng
# Reference:
# https://github.com/dannyweng

# import modules
try:
	## import argparse for future implementations
	import sys
	from modules import urlScan
	from modules import unShortenLink
	from modules import virusTotal
	from modules import whoisquery


# Any import errors print to screen and exit
except (Exception, error):
	print ('error')
	sys.exit(1)

user_input = unShortenLink.shortenLink(input("\nPlease provide a link you want analyzed : \n\n"))

# Comment out any of the tools below if you don't want the output from certain tools:

urlScan.urlScanFunc(user_input)    ## urlScan.io
virusTotal.vtFunc(user_input)    ## VirusTotal
whoisquery.whois(user_input)	## whois

print('\nThe script opened up a few tabs for you to review.\n\n\
fyi: it takes urlscan about a whole minute to scan the site so wait a minute and refresh page')