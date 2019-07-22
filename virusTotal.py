# To run link through unshorten incase the link is shorten

import requests, time, webbrowser
import config

if __name__ == '__main__':

VirusTotalApiKey = config.vtAPIKey

# targetLink = input('What is the link being analyzed? ')
linkUnshortener = requests.get('https://unshorten.me/json/{}'.format(targetLink))
# print(linkUnshortener.text)
linkUnshortener_json = linkUnshortener.json()
print('Requested link : ' + linkUnshortener_json['requested_url'] +
       '\nUnshortened link : ' + linkUnshortener_json['resolved_url'])

resolvedLink = linkUnshortener_json['resolved_url']

if resolvedLink == '':
       print('That is not a valid link! Please double check your link input.')
       exit()
else:
       # To process through Virustotal after
       url = 'https://www.virustotal.com/vtapi/v2/url/scan'
       params = {'apikey': VirusTotalApiKey, 'url':'{}'.format(resolvedLink)}
       response = requests.post(url, data=params)
       response_json = response.json()
       # print(response_json)
       url = response_json['permalink']
       time.sleep(1)  # it takes a while for urlscan to finish preparing the results over 60 seconds normally
       webbrowser.open(url, new=0, autoraise=True)