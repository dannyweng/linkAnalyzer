# API from virustotal

import requests, time, webbrowser
import config

def vtFunc(link):
    
    VirusTotalApiKey = config.vtAPIKey
        
    # To process through Virustotal after
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': VirusTotalApiKey, 'url':'{}'.format(link)}
    response = requests.post(url, data=params)
    response_json = response.json()
    # print(response_json)
    url = response_json['permalink']
    time.sleep(1)  # it takes a while for urlscan to finish preparing the results over 60 seconds normally
    webbrowser.open(url, new=0, autoraise=True)