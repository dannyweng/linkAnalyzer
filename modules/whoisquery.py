import whois
    # import datetime

def whois(link):

    w = whois.whois (link)
    # w = whois.whois ('google.com')
    # w = w.expiration_date  # dates converted to datetime object
    # datetime.datetime(2013, 6, 26, 0, 0)
    # w = w.text  # the content downloaded from whois server
    # u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net'

    print ('The WhoIs Output: \n')
    print (w)

# keylist = ['domain_name', 'registrar', 'whois_server', 'updated_date', 'creation_date', 'expiration_date', 'name_servers', 'emails', 'dnssec', 'name', 'org', 'address', 'city', 'state', 'zipcode', 'country']
