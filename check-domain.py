import whois


def is_registered(domain_name):
    try:
        domain = whois.whois(domain_name)
        if domain['status'] == None:
            print('{} is available'.format(domain_name))
        else:
            print('{} is not available'.format(domain_name))
    except:
        print('{} is available'.format(domain_name))


if __name__ == "__main__":
    is_registered('google.com')
    is_registered('uol.com')
    is_registered('askdiejfir.com')
