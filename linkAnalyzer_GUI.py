#! /usr/bin/env python

# Link Analyzer Script/Toolkit
# Author: Danny Weng
# Reference:
# https://github.com/dannyweng

try:
	## import argparse for future implementations
    import sys
    import PySimpleGUI as sg
    import subprocess    
    from modules import urlScan
    from modules import unShortenLink
    from modules import virusTotal
    from modules import whoisquery
    

# Any import errors print to screen and exit
except (Exception, error):
	print ('error')
	sys.exit(1)

# Please check Demo programs for better examples of launchers      
def ExecuteCommandSubprocess(command, *args):      
    try:      
        sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      
        out, err = sp.communicate()      
        if out:      
            print(out.decode("utf-8"))      
        if err:      
            print(err.decode("utf-8"))      
    except:      
        pass      


layout = [      
    [sg.Text('1. Input URL    2. Click on desired script or hit ENTER to run all', size=(50, 1))],      
    [sg.Output(size=(88, 20))],      
    [sg.Button('unShorten Link'), sg.Button('urlScan'), sg.Button('VirusTotal'), sg.Button('WhoIs')],      
    [sg.Text('Paste link here:', size=(15, 1)), sg.InputText(focus=True), sg.Button('Run All', bind_return_key=True), sg.Button('EXIT')]      
        ]      


window = sg.Window('Script launcher - by Danny Weng', layout)      

# ---===--- Loop taking in user input and using it to call scripts --- #      


while True:      
  (event, value) = window.Read()      
  if event == 'EXIT'  or event is None:  
      break # exit button clicked  
  if event == 'unShorten Link':  
      unShortenLink.shortenLink(value[0]) # unshorten link
  elif event == 'urlScan':  
      urlScan.urlScanFunc(value[0])    ## urlScan.io 
  elif event == 'VirusTotal':  
      virusTotal.vtFunc(value[0])    ## VirusTotal
  elif event == 'WhoIs':  
      whoisquery.whois(value[0])    ## WhoIs
  elif event == 'Run All':      
    #   ExecuteCommandSubprocess(value[0])
      user_input = unShortenLink.shortenLink(value[0]) # unshorten link
      urlScan.urlScanFunc(user_input)    ## urlScan.io
      virusTotal.vtFunc(user_input)    ## VirusTotal
      whoisquery.whois(user_input)    ## WhoIs
      print ('\nThe script opened up a few tabs for you to review.\n\nfyi: it takes urlscan about a whole minute to scan the site so wait a minute and refresh page')