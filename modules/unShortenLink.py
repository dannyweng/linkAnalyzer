# API from unshorten.me

import requests

def shortenLink(raw_link):
        
    while ' ' in raw_link:
        print('Your input has a space.')
        break
    # while '' in raw_link:
    #     print('You didnt input anything!')
    #     break

    linkUnshortener = requests.get(f'https://unshorten.me/json/{raw_link}')
    # print(linkUnshortener.text)
    
    linkUnshortener_json = linkUnshortener.json()

    if raw_link == linkUnshortener_json['resolved_url']:
        print('\nCant unshorten the provided link any further.' +
            '\n\nRequested link : ' + str(raw_link))
        resolvedLink = raw_link
        return resolvedLink
    
    else:
        print('\nRequested link : ' + linkUnshortener_json['requested_url'] +
            '\nUnshortened link : ' + linkUnshortener_json['resolved_url'])

        resolvedLink = linkUnshortener_json['resolved_url']
        
        if resolvedLink == '':
            print('\nEither the provided link cant be shortened anymore or your input was an invalid link.')
            # exit()
            resolvedLink = linkUnshortener_json['requested_url']
        
        return resolvedLink
