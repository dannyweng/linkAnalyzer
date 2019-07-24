# API from unshorten.me

import requests

def shortenLink(raw_link):
        
    if raw_link == ('' or ' '):
       print('You didnt enter a valid link! Please double check your link input.')
       exit()
       
    linkUnshortener = requests.get('https://unshorten.me/json/{}'.format(raw_link))
    
    # print(linkUnshortener.text)
    
    linkUnshortener_json = linkUnshortener.json()
    print('\nRequested link : ' + linkUnshortener_json['requested_url'] +
        '\nUnshortened link : ' + linkUnshortener_json['resolved_url'])

    resolvedLink = linkUnshortener_json['resolved_url']
    
    if resolvedLink == '':
        print('The provided link is invalid, please check your input to see if you actually entered a link.')
        exit()
    
    return resolvedLink

    