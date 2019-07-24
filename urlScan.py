# API from urlscan.io

import requests, webbrowser, time, config

def urlScanFunc(link):
    apikey = config.urlScanAPIKey
    
    urlRequest = link

    headers = {
        'Content-Type': 'application/json',
        'API-Key': apikey,
    }
    print(urlRequest)
    data = '{"url": "'+ f"{urlRequest}" + '", "public": "on", "tags": ["phishing", "malicious"]}'

    # print(data)

    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=data)

    # print(response.text)

    response_json = response.json()

    url = response_json['result']
    time.sleep(1)  # it takes a while for urlscan to finish preparing the results over 60 seconds normally
    webbrowser.open(url, new=0, autoraise=True)
    
# urlScanFunc('google.com') # Just to test script
