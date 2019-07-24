# API from unshorten.me

import requests

def shortenLink(raw_link):
        
    if raw_link == ('' or ' '):
       print('You didnt enter a valid link! Please double check your link input.')
       exit()

    linkUnshortener = requests.get(f'https://unshorten.me/json/{raw_link}')
    # print(linkUnshortener.text)
    
    linkUnshortener_json = linkUnshortener.json()

    if raw_link != linkUnshortener_json['requested_url']:
        print('\nCant unshorten provided link so I will push it through the tools as is.' +
            '\n\nRequested link : ' + str(raw_link))
        resolvedLink = raw_link
        return resolvedLink
    
    else:
        print('\nRequested link : ' + linkUnshortener_json['requested_url'] +
            '\nUnshortened link : ' + linkUnshortener_json['resolved_url'])

        resolvedLink = linkUnshortener_json['resolved_url']
        
        if resolvedLink == '':
            print('\nThe provided link is invalid, please check your input to see if you actually entered a link.')
            exit()
        
        return resolvedLink

    