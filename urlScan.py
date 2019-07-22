import requests, webbrowser, time, config

apikey = config.urlScanAPIKey

urlRequest = input('Enter a URL in this form (google.com) :')
# '"google.com"'
headers = {
    'Content-Type': 'application/json',
    'API-Key': apikey,
}
print(urlRequest)
data = '{"url": "'+ f"{urlRequest}" + '", "public": "on", "tags": ["phishing", "malicious"]}'

print(data)

response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=data)

print(response.text)

response_json = response.json()

print(response_json['result'])

url = response_json['result']
time.sleep(1)  # it takes a while for urlscan to finish preparing the results over 60 seconds normally
webbrowser.open(url, new=0, autoraise=True)